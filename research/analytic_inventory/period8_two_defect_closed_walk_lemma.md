# Exact closed-walk lemma for the non-antipodal two-defect phases

This lemma is the deliberately finite part of the period-eight trichotomy.
It is a recurrence calculation over integers, not a spectral approximation,
search over signings, or floating-point certificate.

## Statement

Let \(Q\) be an eight-periodic local quadrilateral-flux word with exactly two
positive entries, at positions \(0\) and \(s\), where \(s\in\{1,2,3\}\), and
let \(\tau_0=1\), \(\tau_{i+1}=Q_i\tau_i\).  Put

\[
M_k=\sum_{r=0}^{7}(A_\tau^{\,2k})_{r,r},
\qquad E_k=M_{k+1}-8M_k.
\]

Then the first positive \(E_k\) is respectively

\[
E_4=5504\quad(s=1),\qquad
E_6=64336\quad(s=2),\qquad
E_9=2872096\quad(s=3).
\]

Consequently the squared Bloch spectral edge is strictly larger than \(8\)
in each of these three cases.

## Exact recurrence

For a starting residue \(r\), let \(f^{(r)}_\ell(j)\) be the signed sum of
all length-\(\ell\) walks from \(r\) to \(j\) in the Hamilton gauge.  Start
with \(f^{(r)}_0(j)=\mathbf 1_{j=r}\), extend \(\tau\) periodically, and use

\[
f^{(r)}_{\ell+1}(j)=f^{(r)}_\ell(j-1)+f^{(r)}_\ell(j+1)
 +\tau_{j-2}f^{(r)}_\ell(j-2)+\tau_j f^{(r)}_\ell(j+2).
\tag{1}
\]

Then \(M_k=\sum_{r=0}^{7}f^{(r)}_{2k}(r)\).  Formula (1) only involves
integer additions and signs.  For the largest displayed calculation it has
length \(20\) and support in \([-40,47]\), so the following table can be
checked directly by hand or by a short exact recurrence.

\[
\begin{array}{c|rrrrrrrrrr}
s\backslash k&1&2&3&4&5&6&7&8&9&10\\ \hline
1&32&192&1376&10976&93312&&&&&\\
2&32&192&1328&9888&76832&612624&4965328&&&\\
3&32&192&1280&9056&66592&503088&3877920&30363808&240761792&1928966432
\end{array}
\]

The corresponding excesses through the first positive entry are

\[
\begin{array}{c|rrrrrrrrr}
s\backslash k&1&2&3&4&5&6&7&8&9\\ \hline
1&-64&-160&-32&5504\\
2&-64&-208&-736&-2272&-2032&64336\\
3&-64&-256&-1184&-5856&-29648&-146784&-659552&-2148672&2872096
\end{array}
\]

## Why a positive excess proves the claim

For a Bloch fiber \(H(z)\), write \(R\) for the supremum of its squared
spectral radius over \(|z|=1\).  The normalized fiber trace representation
of \(M_k\) is an average of nonnegative numbers \(\lambda^{2k}\).  If
\(R\le8\), pointwise \(\lambda^{2k+2}\le8\lambda^{2k}\), hence
\(M_{k+1}\le8M_k\).  Each displayed positive \(E_k\) contradicts this
inequality.

The other lift \(-\tau\) has the same squared spectrum, so the result is a
statement about \(Q\), not about the selected normalization \(\tau_0=1\).

## Evidence boundary

This is a finite exact lemma.  It is intentionally retained as such in a
future manuscript, rather than being described as a general analytic
classification argument.  The recurrence is independently replayed in
research/scripts/verify_target_a_period8_analytic_package.py.
