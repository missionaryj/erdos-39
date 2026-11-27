import OMAReductions.R_Erdos39_erdos_39_R1

-- Compactness step for @missionaryj. The finite-coordinate subsequence
-- argument follows OMA.Erdos28DensityTransfer.infinite_counterexample in
-- reductions/Erdos28.erdos_28.R1.H1.R2.lean in open-math-agents.

open Filter
open scoped Topology

theorem OMA.solution : OMA.R_Erdos39_erdos_39_R1.H2 := by
  classical
  intro f hunbounded hfinite
  choose B sidon count using hfinite
  let bits (K j : ℕ) : Bool := decide (j ∈ B K)
  obtain ⟨v, φ, hφ, ht⟩ := CompactSpace.tendsto_subseq bits
  let A : Set ℕ := {j | v j = true}
  have agree (n : ℕ) : ∃ K ≥ n, ∀ j ≤ n, j ∈ A ↔ j ∈ B K := by
    have coord (j : ℕ) : ∀ᶠ k in atTop, bits (φ k) j = v j := by
      have h := tendsto_pi_nhds.mp ht j
      rw [nhds_discrete Bool] at h
      exact tendsto_pure.mp h
    have window : ∀ᶠ k in atTop, ∀ j ∈ Finset.Iic n, bits (φ k) j = v j :=
      (eventually_all_finset _).mpr (fun j _ => coord j)
    obtain ⟨k, hk, hw⟩ := ((eventually_ge_atTop n).and window).exists
    refine ⟨φ k, hk.trans (hφ.id_le k), ?_⟩
    intro j hj
    change v j = true ↔ _
    rw [← hw j (Finset.mem_Iic.mpr hj)]
    simp [bits]
  have bound (n : ℕ) : f n ≤ ((Set.Icc 1 n) ∩ A).ncard := by
    obtain ⟨K, hn, ha⟩ := agree n
    have eq : (Set.Icc 1 n) ∩ A = (Set.Icc 1 n) ∩ (B K : Set ℕ) := by
      ext j
      constructor
      · rintro ⟨hj, h⟩
        exact ⟨hj, (ha j hj.2).mp h⟩
      · rintro ⟨hj, h⟩
        exact ⟨hj, (ha j hj.2).mpr h⟩
    rw [eq]
    exact count K n hn
  refine ⟨A, ?_, ?_, bound⟩
  · intro hA
    obtain ⟨n, hn⟩ := hunbounded (A.ncard + 1)
    have small : ((Set.Icc 1 n) ∩ A).ncard ≤ A.ncard :=
      Set.ncard_le_ncard Set.inter_subset_right hA
    have h := bound n
    omega
  · intro a ha b hb c hc d hd he
    obtain ⟨K, _, row⟩ := agree (max (max a b) (max c d))
    exact sidon K a ((row a (by omega)).mp ha) b ((row b (by omega)).mp hb)
      c ((row c (by omega)).mp hc) d ((row d (by omega)).mp hd) he
