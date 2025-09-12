# Complete Daily GW arXiv Digest - 2025-09-12

**总爬取文章**: 141 篇  
**今天的文章**: 141 篇  
  - gr-qc: 17 篇  
  - astro-ph: 114 篇  
**引力波相关**: 15 篇  
**提交类型**: 🆕 4 New • 🔄 5 Cross-lists • 🔄 6 Replacements  

## 1. Systematic errors in fast relativistic waveforms for Extreme Mass Ratio Inspirals

**arXiv**: [2509.08875](https://arxiv.org/abs/2509.08875)  
**Authors**: Hassan Khalvati, Philip Lynch, Ollie Burke, Lorenzo Speri, Maarten van de Meent, Zachary Nasipak  
**Date**: 12 Sep 2025  
**Categories**: gr-qc  
**Type**: new submission  

**Abstract**: Systematic errors in fast relativistic waveforms for Extreme Mass Ratio Inspirals Hassan Khalvati, Philip Lynch, Ollie Burke, Lorenzo Speri, Maarten van de Meent, Zachary Nasipak General Relativity and Quantum Cosmology (gr-qc) Accurate modeling of Extreme Mass-Ratio Inspirals (EMRIs) is essential for extracting reliable information from future space-based gravitational wave observatories. Fast waveform generation frameworks adopt an offline/online architecture, where expensive relativistic computations (e.g. self-force and black hole perturbation theory) are performed offline, and waveforms are generated rapidly online via interpolation across a multidimensional parameter space. In this work, we investigate potential sources of error that result in systematic bias in these relativistic waveform models, focusing on radiation-reaction fluxes. Two key sources of systematics are identified: (i) the intrinsic inaccuracy of the flux data, for which we focus on the truncation of the multipolar mode sum, and (ii) interpolation errors from transitioning to the online stage. We quantify the impact of mode-sum truncation and analyze interpolation errors by using various grid structures and interpolation schemes. For circular orbits in Kerr spacetime with spins larger than $a \geq 0.9$, we find that $\ell_{\text{max}} \geq 30$ is required for the necessary accuracy. We also develop an efficient Chebyshev interpolation scheme, achieving the desired accuracy level with significantly fewer grid points compared to spline-based methods. For circular orbits in Kerr spacetimes, we demonstrate via Bayesian studies that interpolating the flux to a maximum global relative error that is equal to the small mass ratio is sufficient for parameter estimation purposes. For 4-year long quasi-circular EMRI signals with SNRs$= \mathcal{O}(100)$ and mass-ratios $10^{-4}-10^{-6}$, a global relative error of $10^{-6}$ yields mismatches $<10^{-3}$ and negligible parameter estimation biases.  

---

## 2. Probing Direct Waves in Black Hole Ringdowns

**arXiv**: [2509.09165](https://arxiv.org/abs/2509.09165)  
**Authors**: Naritaka Oshita, Sizheng Ma, Yanbei Chen, Huan Yang  
**Date**: 12 Sep 2025  
**Categories**: gr-qc  
**Type**: new submission  

**Abstract**: Probing Direct Waves in Black Hole Ringdowns Naritaka Oshita, Sizheng Ma, Yanbei Chen, Huan Yang General Relativity and Quantum Cosmology (gr-qc) Merger gravitational waves from binary black hole coalescence carry rich information about the underlying spacetime dynamics. We analyze merger waves from comparable-mass and extreme-mass-ratio binaries, obtained from numerical relativity and black-hole perturbation theory, respectively, and argue that they are dominated by the prompt wave emissions as the black holes collide. This signal, which we refer to as the direct wave, is modulated by the plunging motion and selectively screened by the gravitational potential of the remnant black hole. The direct wave typically exhibits a time-dependent frequency and decay rate, but for high-spin remnants $(\gtrsim0.7)$ the ergosphere renders it mode-like, with a quasi-stable instantaneous oscillation frequency close to the superradiant frequency. We further estimate its detectability in a GW150914-like system and find that the signal-to-noise ratio can exceed $\sim 10$ with the current ground-based detector network. Our results therefore identify the direct wave as a robust observable for analyzing black hole ringdowns in current and future gravitational wave events.  

---

## 3. Ultralight Boson Ionization from Comparable-Mass Binary Black Holes

**arXiv**: [2509.09643](https://arxiv.org/abs/2509.09643)  
**Authors**: Yuhao Guo, Zhen Zhong, Yifan Chen, Vitor Cardoso, Taishi Ikeda, Lihang Zhou  
**Date**: 12 Sep 2025  
**Categories**: gr-qc, astro-ph.CO, astro-ph.HE, hep-ph  
**Type**: new submission  

**Abstract**: Ultralight Boson Ionization from Comparable-Mass Binary Black Holes Yuhao Guo, Zhen Zhong, Yifan Chen, Vitor Cardoso, Taishi Ikeda, Lihang Zhou 18 pages, 5 figures, movie: this https URL General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO); High Energy Astrophysical Phenomena (astro-ph.HE); High Energy Physics - Phenomenology (hep-ph) Ultralight bosons around comparable-mass binaries can form gravitationally bound states analogous to molecules once the binary separation decreases below the boson's Bohr radius, with the inner region co-moving with the binary. We simulate the formation of these gravitational molecules, determine their co-moving regions, and compute ionization fluxes induced by orbital motion for various binary eccentricities. We develop semi-analytic formalisms to describe the ionization dynamics of both the co-moving and non-co-moving regions, demonstrating consistency with numerical simulation results. From ionization fluxes, we estimate their backreaction on binary orbital evolution. At early stages, molecule ionization can dominate over gravitational wave emission, producing a spectral turnover in the gravitational wave background. Additionally, ionization of the co-moving component occurs solely due to binary eccentricity, causing orbital circularization.  

---

## 4. Machine Learning Confirms GW231123 is a "Lite" Intermediate Mass Black Hole Merger

**arXiv**: [2509.09161](https://arxiv.org/abs/2509.09161)  
**Authors**: Chayan Chatterjee, Kaylah McGowan, Suyash Deshmukh, Karan Jani  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.HE, gr-qc  
**Type**: cross-list from astro-ph.HE  

**Abstract**: Machine Learning Confirms GW231123 is a "Lite" Intermediate Mass Black Hole Merger Chayan Chatterjee, Kaylah McGowan, Suyash Deshmukh, Karan Jani High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) The LIGO-Virgo-KAGRA Collaboration recently reported GW231123, a black hole merger with total mass of around 190-265 solar mass. This event adds to the growing evidence of "lite" intermediate mass black hole (IMBH) discoveries of post-merger black holes >100 solar mass. GW231123 posed several data analysis challenges owing to waveform-model systematics and presence of noise artifacts called glitches. We present the first comprehensive machine learning analysis to further validate this event, strengthen its astrophysical inference, and characterize instrumental noise in its vicinity. Our approach uses a combination of tools tailored for specific analyses: GW-Whisper, an adaptation of OpenAI's audio transformer, ArchGEM, a Gaussian mixture model-based soft clustering and density approximation software and AWaRe, a convolutional autoencoder. We identify the data segment containing the merger with >70% confidence in both detectors and verify its astrophysical origin. We then characterize the scattered light glitch around the event, providing the first physically interpretable parameters for the glitch. We also reconstruct the real waveforms from the data with slightly better agreement to model-agnostic reconstructions than to quasi-circular models, hinting at possible astrophysics beyond current waveform families (such as non-circular orbits or environmental imprints). Finally, by demonstrating high-fidelity waveform reconstructions for simulated mergers with total masses between 100-1000 solar mass, we show that our method can confidently probe the IMBH regime. Our integrated framework offers a powerful complementary tool to traditional pipelines for rapid, robust analysis of massive, glitch-contaminated events.  

---

## 5. Towards systematic search for white dwarf binaries with multiband photometry

**arXiv**: [2509.09348](https://arxiv.org/abs/2509.09348)  
**Authors**: Alice Perego, Astrid Lamberts, Mathias Schultheis, Nelson Christensen  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.HE, gr-qc  
**Type**: cross-list from astro-ph.HE  

**Abstract**: Towards systematic search for white dwarf binaries with multiband photometry Alice Perego, Astrid Lamberts, Mathias Schultheis, Nelson Christensen High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) Ultra-compact double white dwarfs (DWDs) represent key targets for multi-messenger astrophysics, as they may be observed both through gravitational waves and the electromagnetic (EM) spectrum. The future Laser Interferometer Space Antenna (LISA) will detect thousands of these systems, and they are predicted to be the most numerous science targets of the mission. We develop a strategy to identify LISA source candidates in multiband photometric surveys. We constructed a synthetic EM catalogue of white dwarf (WD) detections based on a population synthesis code combined with a semi-analytical model of the Milky Way and a consistent cooling model for the evolution. We compared sources in the LISA band with other WD observations in magnitude-colour and colour-colour plots. From a full sky survey with $u \le$24.5, we find that 57$\%$ of the sources in the LISA band occupy a specific region in colour-colour diagrams. Inside this area, we find that $\sim 63\%$ (6.5 $\times 10^4$) of EM observations are LISA candidates, $\sim 31\%$ ($ 3.2 \times 10^4$) are DWDs slightly outside the LISA frequency range, and only a small contamination comes from single WDs and wider binaries. We find that the colour distributions of close DWDs represent a powerful tool to distinguish potential LISA sources from the broader WD population. This is an avenue to select candidates for further follow-up and identification.  

---

## 6. Nonlinear Independent Component Analysis Scheme and its application to gravitational wave data analysis

**arXiv**: [2509.09632](https://arxiv.org/abs/2509.09632)  
**Authors**: Jun'ya Kume, Koh Ueno, Tatsuki Washimi, Jun'ichi Yokoyama, Takaaki Yokozawa, Yousuke Itoh  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.IM, gr-qc  
**Type**: cross-list from astro-ph.IM  

**Abstract**: Nonlinear Independent Component Analysis Scheme and its application to gravitational wave data analysis Jun'ya Kume, Koh Ueno, Tatsuki Washimi, Jun'ichi Yokoyama, Takaaki Yokozawa, Yousuke Itoh Instrumentation and Methods for Astrophysics (astro-ph.IM); General Relativity and Quantum Cosmology (gr-qc) Noise subtraction is a crucial process in gravitational wave (GW) data analysis to improve the sensitivity of interferometric detectors. While linear noise coupling has been extensively studied and successfully mitigated using methods such as Wiener filtering, subtraction of non-linearly coupled and non-stationary noise remains a significant challenge. In this work, we propose a novel independent component analysis (ICA)-based framework designed to address non-linear coupling in noise subtraction. Building upon previous developments, we derive a method to estimate general quadratic noise coupling while maintaining computational transparency compared to machine learning approaches. The proposed method is tested with simulated data and real GW strain data from KAGRA. Our results demonstrate the potential of this framework to effectively mitigate complex noise structures, providing a promising avenue for improving the sensitivity of GW detectors.  

---

## 7. From Geometry to Observation: Gravitational Waves and the Raychaudhuri Equation

**arXiv**: [2504.09562](https://arxiv.org/abs/2504.09562)  
**Authors**: Sougata Bhunia, Anubhab Dutta, Debashis Gangopadhyay, Goutam Manna  
**Date**: 12 Sep 2025  
**Categories**: gr-qc  
**Type**: replaced  

**Abstract**: From Geometry to Observation: Gravitational Waves and the Raychaudhuri Equation Sougata Bhunia, Anubhab Dutta, Debashis Gangopadhyay, Goutam Manna 19 pages, 10 figures, 6 tables, Accepted from Physics of the Dark Universe General Relativity and Quantum Cosmology (gr-qc) Gravitational waves (GWs) are independent of any particular theory of gravity. The universality of this notion is highlighted by the Raychaudhuri equation (RE), which is independent of any theory of gravity and contains the Ricci tensor $R_{\mu\nu}$ as a key ingredient, thereby connecting spacetime geometry with matter-energy content. Under small metric perturbations, $R_{\mu\nu} \propto \Box h_{\mu\nu}$, where $h_{\mu\nu}$ is the perturbation, indicating that various gravity theories, via their corresponding $R_{\mu\nu}$, produce different gravitational wave equations. In the framework of Einstein's gravity, this leads to the standard wave equation. This study analyzes a modified form, {\it GW-inspired RE}, within the homogeneous and isotropic FLRW background to investigate late-time cosmic acceleration and structure formation. We employ {\it Pantheon+ SNe Ia, Hubble, and BAO} datasets to constrain model parameters through Bayesian inference utilizing NUTS in {\it NumPyro}. A nuisance parameter $\mu_0$ is introduced to address residual systematics. This facilitates a robust estimation of $H_0$, $\Omega_{DE,0}$, and $r_d$, which addresses the resolution of the Hubble tension. We analyze the redshift evolution of the deceleration parameter, $q(z)$, both with and without $\mu_0$, emphasizing its influence on cosmic dynamics. The GW-inspired RE is reformulated as a harmonic oscillator, providing insight into expansion and geodesic focusing. A graphical comparison demonstrates the relationship $d^{GW}_L(z) = d^{EM}_L(z)$ utilizing GWOSC data. Thus, the RE in the context of small perturbation of the metric opens up whole new vistas of {\it observational astronomy.}  

---

## 8. Primordial Black Hole Formation from the Upward Step Model: Avoiding Overproduction

**arXiv**: [2412.19631](https://arxiv.org/abs/2412.19631)  
**Authors**: Xiaoding Wang, Xiao-Han Ma, Yi-Fu Cai  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.CO, gr-qc  
**Type**: replaced  

**Abstract**: Primordial Black Hole Formation from the Upward Step Model: Avoiding Overproduction Xiaoding Wang, Xiao-Han Ma, Yi-Fu Cai Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc) We investigate the formation of primordial black holes (PBHs) in an upward step inflationary model, where nonlinearities between curvature perturbations and field fluctuations introduce a cutoff, deviating from the Gaussian case. This necessitates a reevaluation of PBH formation, as $\mathcal{R}$ is not the optimal variable for estimating abundance. Using the extended Press-Schechter formalism, we show that non-Gaussianity modifies both the curvature perturbation profile $\mathcal{R}(r)$ and the integration path in probability space, significantly impacting PBH abundance. Our results reveal that the abundance initially increases with the parameter $h$, which characterizes the relaxation stage after the step. However, beyond a critical value ($h \simeq 5.9$), it sharply declines before rising again. Furthermore, we demonstrate that non-Gaussianity introduces uncertainties in indirect PBH observations via gravitational waves. Notably, we present an example where a positive $f_{\rm NL}$ does not necessarily enhance PBH production, contrary to conventional expectations. Finally, by accounting for non-perturbative effects, we resolve the overproduction of PBHs suggested by pulsar timing array (PTA) data, underscoring the critical importance of incorporating non-Gaussianity in future studies.  

---

## 9. Isotropy, anisotropies and non-Gaussianity in the scalar-induced gravitational-wave background: diagrammatic approach for primordial non-Gaussianity up to arbitrary order

**arXiv**: [2505.16820](https://arxiv.org/abs/2505.16820)  
**Authors**: Jun-Peng Li, Sai Wang, Zhi-Chao Zhao, Kazunori Kohri  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.CO, gr-qc, hep-ph  
**Type**: replaced  

**Abstract**: Isotropy, anisotropies and non-Gaussianity in the scalar-induced gravitational-wave background: diagrammatic approach for primordial non-Gaussianity up to arbitrary order Jun-Peng Li, Sai Wang, Zhi-Chao Zhao, Kazunori Kohri 107 pages, 36 figures. Version 2: Added discussions on the infrared scaling of the SIGW energy-density spectra in Section 6 and the Appendix. Corrected the calculation of PBH abundance in Section 6. Corrected some typos and included several new references Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph) Produced nonlinearly by the enhanced linear cosmological curvature perturbations, the scalar-induced gravitational waves (SIGWs) can serve as a potentially powerful probe of primordial non-Gaussianity (PNG) in the early Universe. In this work, we comprehensively investigate the imprints of local-type PNG on the SIGW background beyond the widely used quadratic and cubic approximations. We develop a diagrammatic approach capable of analyzing SIGWs for PNG up to arbitrary order. Following this approach, we derive semi-analytic formulas for the energy-density fraction spectrum, the angular power spectrum, and the angular bispectrum and trispectrum to describe the isotropic component, anisotropies, and non-Gaussianity of the SIGW background, respectively. Particularly, focusing on PNG up to quartic approximation (parameterized by $f_\mathrm{NL}$, $g_\mathrm{NL}$, and $h_\mathrm{NL}$), we numerically compute all contributions to these SIGW spectra. We find that PNG can significantly alter the magnitude of the SIGW energy-density spectrum, and can generate substantial anisotropies through the initial inhomogeneities in the SIGW distribution. Furthermore, we observe that the SIGW angular bispectrum and trispectrum always vanish when the primordial curvature perturbations are Gaussian; otherwise, they do not, indicating their potential utility as probes of PNG. Therefore, we anticipate that the SIGW background will provide essential information about the early Universe.  

---

## 10. Towards high-precision inspiral gravitational waveforms from binary neutron star mergers in numerical relativity

**arXiv**: [2508.10981](https://arxiv.org/abs/2508.10981)  
**Authors**: Kenta Kiuchi  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.HE, gr-qc  
**Type**: replaced  

**Abstract**: Towards high-precision inspiral gravitational waveforms from binary neutron star mergers in numerical relativity Kenta Kiuchi 14 pages, 8 figures, PRD accepted High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) We report the performance of a newly implemented fourth-order accurate finite-volume HLLC Riemann solver in the adaptive-mesh-refinement numerical relativity code {\tt SACRA-MPI}. First, we validate our implementation in one-dimensional special relativistic hydrodynamics tests, i.e., a simple wave and shock tube test, which have analytic solutions. We demonstrate that the fourth-order convergence is achieved for the smooth flow, which cannot be achieved in our original second-order accurate finite-volume Riemann solver. We also show that our new solver is robust for the strong shock wave emergence problem. Second, we validate the implementation in a dynamical spacetime by demonstrating that {\tt SACRA-MPI} perfectly preserves the $\pi$-symmetry without imposing the $\pi$-symmetry in a short-term ($\sim 20~{\rm ms}$ in the inspiral and subsequent post-merger phase) non-spinning equal-mass binary neutron star merger simulations. Finally, we quantify the accuracy of $\approx 28$ cycles inspiral gravitational waveforms from binary neutron star mergers by conducting a resolution study with $\approx 78, 94$, $118$, and $135$ m. We find that the fourth-order accurate Riemann solver achieves the convergence order $\approx 2.1\pm{0.05}$--$2.4\pm{0.27}$, i.e., slightly evolving with time, in the inspiral gravitational wave phase, while the second-order accurate Riemann solver achieves the convergence order $\approx 2.0\pm{0.5}$. The residual phase error towards the continuum limit at the merger is $0.27\pm 0.07$ rad and $0.58\pm 0.22$ rad out of a total phase of $\approx 176$ rad, respectively, for the fourth- and second-order accurate Riemann solver.  

---

## 11. Inflation using a triplet of Antisymmetric tensor fields

**arXiv**: [2212.13508](https://arxiv.org/abs/2212.13508)  
**Authors**: Abhijith Ajith, Sukanta Panda  
**Date**: 12 Sep 2025  
**Categories**: gr-qc, astro-ph.CO  
**Type**: cross-list from gr-qc  

**Abstract**: Inflation using a triplet of Antisymmetric tensor fields Abhijith Ajith, Sukanta Panda General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO) We study an inflation model driven by a triplet of antisymmetric tensor fields, with minimal and nonminimal couplings to gravity. First, we show that the presence of a triplet of antisymmetric tensor fields can provide inherent background isotropy in the stress-energy tensor contrary to the past studies using an antisymmetric tensor field. Inflation is supported in the presence of non-minimal couplings with gravity. We perform the slow roll analysis and also analyse perturbations to the antisymmetric tensor field as well as the tensor modes of perturbed metric. The speed of gravitational waves manifested from the tensor perturbations is tuned to $c$. We also study the evolution of the gravitational waves, calculate their power spectrum and tensor spectral index.  

---

## 12. Binary Black Hole Phase Space Discovers the Signature of Pair Instability Supernovae Mass Gap

**arXiv**: [2509.09123](https://arxiv.org/abs/2509.09123)  
**Authors**: Samsuzzaman Afroz, Suvodip Mukherjee  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.HE, astro-ph.CO  
**Type**: cross-list from astro-ph.HE  

**Abstract**: Binary Black Hole Phase Space Discovers the Signature of Pair Instability Supernovae Mass Gap Samsuzzaman Afroz, Suvodip Mukherjee High Energy Astrophysical Phenomena (astro-ph.HE); Cosmology and Nongalactic Astrophysics (astro-ph.CO) The rapidly expanding catalog of gravitational-wave detections provides a powerful probe of the formation history of compact binaries across cosmic time. In this work, we extend the Binary Compact Object (BCO) phase-space framework to the full set of events in the GWTC-4 catalog to map the observed binary formation scenarios in a data-driven way. Applying this framework, we identify distinct regions of phase-space associated with different channels and discover for the first time a unique mass-cutoff scale in a data-driven way. The mapping of these on different formation channels reveals a population of first-generation (1G) black holes sharply truncated at approximately 45.5 $M_\odot$, consistent with the theoretically predicted pair-instability supernova (PISN) mass gap. These findings demonstrate the capability of the BCO phase-space to disentangle overlapping formation pathways, establish robust connections between gravitational-wave observations and binary evolution, and highlight the potential of upcoming observing runs to reveal rare populations and exotic origins.  

---

## 13. The Bearable Inhomogeneity of the Baryon Asymmetry

**arXiv**: [2505.15904](https://arxiv.org/abs/2505.15904)  
**Authors**: Hengameh Bagherian, Majid Ekhterachian, Stefan Stelzl  
**Date**: 12 Sep 2025  
**Categories**: hep-ph, astro-ph.CO  
**Type**: replaced  

**Abstract**: The Bearable Inhomogeneity of the Baryon Asymmetry Hengameh Bagherian, Majid Ekhterachian, Stefan Stelzl High Energy Physics - Phenomenology (hep-ph); Cosmology and Nongalactic Astrophysics (astro-ph.CO) We study the implications of precision measurements of light-element abundances, in combination with the Cosmic Microwave Background, for scenarios of physics beyond the Standard Model that generate large inhomogeneities in the baryon-to-photon ratio. We show that precision Big Bang Nucleosynthesis (BBN) places strong constraints on any mechanism that produces large-scale inhomogeneities at temperatures around or below the TeV scale. In particular, we find that fluctuations of order $25\%$ on comoving length scales larger than the horizon at $T \simeq 3~\mathrm{TeV}$ are incompatible with the observed light-element abundances. This sensitivity to early-universe physics arises because baryon-number inhomogeneities homogenize primarily through diffusion, a slow process. As a result, BBN serves as a novel probe of baryogenesis below the TeV scale, readily ruling out some proposed scenarios in the literature. We discuss the implications for electroweak baryogenesis, and further show that precision BBN provides a new probe of first-order phase transitions that generate gravitational waves in the pHz-mHz frequency range. This yields constraints on the electroweak phase transition, as well as first-order phase transitions that have been suggested as an explanation of the pulsar timing array signal. Finally, we comment on the future prospects for improving this probe.  

---

## 14. Asymmetric emissions of neutrinos in the cooling of rotating proto-neutron stars

**arXiv**: [2507.04784](https://arxiv.org/abs/2507.04784)  
**Authors**: Laura Barrio, Kotaro Fujisawa, Ryuichiro Akaho, Hiroki Nagakura, Shoichi Yamada  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.HE  
**Type**: replaced  

**Abstract**: Asymmetric emissions of neutrinos in the cooling of rotating proto-neutron stars Laura Barrio, Kotaro Fujisawa, Ryuichiro Akaho, Hiroki Nagakura, Shoichi Yamada High Energy Astrophysical Phenomena (astro-ph.HE) We evaluate global asymmetry in the luminosities of neutrinos emitted from rapidly-rotating proto-neutron stars (PNS's). We build axisymmetric models of PNS's in mechanical equilibrium with rotation by adding prescribed angular momentum distributions by hand to non-rotational PNS models, which are extracted from a one-dimensional (spherically symmetric) PNS cooling calculation at different times: \(t=2, 6, 10, 20, 30\)s after a supernova explosion. We then conduct two-dimensional (spatially axisymmetric) neutrino transport calculations on top of them with the matter profiles (and the spacetime geometry) fixed. We find for the rapidly-rotating models with \(T/|W|\sim 5\times 10^{-2}\) that the neutrino luminosity changes by \(\sim 3 \% \) depending on the observer position. We give detailed analyses of the neutrino-hemispheres as well as the neutrino luminosities that are defined observer-wise. We also calculate the low-frequency (\(\lesssim 1{\rm Hz}\)) gravitational waves produced by the neutrinos radiated asymmetrically. We find that those gravitational waves, if emitted from the Galactic center, can be detected by planned detectors such as B-DECIGO, DECIGO and AILA. Finally, we look for crossings in the energy-integrated angular distributions in momentum space for the electron neutrino sector, a signature of the fast flavor conversion. We find them near the PNS surface in all models.  

---

## 15. High-resolution simulations of disc tearing in the GW Orionis triple system

**arXiv**: [2509.09317](https://arxiv.org/abs/2509.09317)  
**Authors**: Alison K. Young  
**Date**: 12 Sep 2025  
**Categories**: astro-ph.SR, astro-ph.EP  
**Type**: new submission  

**Abstract**: High-resolution simulations of disc tearing in the GW Orionis triple system Alison K. Young Solar and Stellar Astrophysics (astro-ph.SR); Earth and Planetary Astrophysics (astro-ph.EP) The disc around the pre-main-sequence triple star system GW Orionis is known from observations to be warped and broken. Theoretical modelling has produced conflicting results regarding the mechanism responsible for breaking the disc. Analytical predictions for the measured parameters of GW Ori suggest the disc is only marginally stable to tearing. We present new high-resolution simulations of GW Ori that replicate the wavelike regime expected in thick, low-turbulence protoplanetary discs for the first time to settle this question. Using the most optimistic values of misalignment and stellar mass ratio allowed by observational constraints, we find that the GW Ori disc can be torn by stellar torques alone, without need for an embedded planet. Even if the disc retains a smooth warp in simulations with similar parameters, it is likely that any small perturbation in the density or temperature structure could cause the disc to break. The new simulations rule out retrograde disc rotation relative to the stellar orbits and tentatively suggest the thicker ($h/r = 0.04$) disc better matches observations. Going forward, we should take care to ensure models of GW Ori and similar systems appropriately represent the propagation of warps. Additionally, analytical predictions are derived from idealized (and often massless) discs and it is useful to assess how each observed disc might deviate from those assumptions, especially in the context of a young and active star-forming neighbourhood.  

---

