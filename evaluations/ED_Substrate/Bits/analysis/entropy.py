"""Graph-general information-theoretic estimators for the Δ program.

NOT spectral: these operate on arbitrary samples (region-state vectors,
summaries), not on Cartesian-grid Fourier spectra. ed-lab's spectral entropy is
grid-specific; only the Shannon kernel idiom is shared. Mutual information uses
a binned (histogram) estimator with a Miller-Madow bias correction, because the
naive plug-in MI is positively biased at finite sample size — truly independent
variables yield a small positive MI without correction.
"""
from __future__ import annotations

import numpy as np


def _entropy_counts(counts: np.ndarray) -> float:
    """Plug-in Shannon entropy (nats) from a count array."""
    n = counts.sum()
    if n == 0:
        return 0.0
    p = counts[counts > 0] / n
    return float(-np.sum(p * np.log(p)))


def _miller_madow(counts: np.ndarray) -> float:
    """Miller-Madow corrected entropy: H_plugin + (K-1)/(2N), K = nonempty bins."""
    n = counts.sum()
    if n == 0:
        return 0.0
    k = int(np.count_nonzero(counts))
    return _entropy_counts(counts) + (k - 1) / (2.0 * n)


def mutual_information(x: np.ndarray, y: np.ndarray, bins: int = 2,
                       correct: bool = True) -> float:
    """Estimate MI(x; y) in nats from paired samples via a 2D histogram.

    x, y          : 1-D arrays of equal length (the ensemble samples).
    bins          : number of bins per axis (quantile-edged for balance).
    correct       : apply Miller-Madow bias correction (recommended).

    MI = H(x) + H(y) - H(x, y). With correction each marginal/joint entropy is
    Miller-Madow corrected, which centers the estimate near 0 for independent
    data (the naive estimator is positively biased).
    """
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()
    assert x.shape == y.shape and x.size > 0

    xe = _quantile_edges(x, bins)
    ye = _quantile_edges(y, bins)
    xi = np.clip(np.digitize(x, xe[1:-1]), 0, bins - 1)
    yi = np.clip(np.digitize(y, ye[1:-1]), 0, bins - 1)

    joint = np.zeros((bins, bins), dtype=float)
    for a, b in zip(xi, yi):
        joint[a, b] += 1.0
    cx = joint.sum(axis=1)
    cy = joint.sum(axis=0)

    if correct:
        hx = _miller_madow(cx)
        hy = _miller_madow(cy)
        hxy = _miller_madow(joint.ravel())
    else:
        hx = _entropy_counts(cx)
        hy = _entropy_counts(cy)
        hxy = _entropy_counts(joint.ravel())
    return hx + hy - hxy


def _quantile_edges(v: np.ndarray, bins: int) -> np.ndarray:
    """Bin edges at quantiles, so each bin holds ~equal mass (robust to scale)."""
    qs = np.linspace(0.0, 1.0, bins + 1)
    edges = np.quantile(v, qs)
    # Ensure strictly increasing edges (degenerate if v is constant).
    eps = 1e-12
    for i in range(1, len(edges)):
        if edges[i] <= edges[i - 1]:
            edges[i] = edges[i - 1] + eps
    return edges
