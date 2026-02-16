# Complete Daily GW arXiv Digest - 2026-02-16

**总爬取文章**: 163 篇  
**今天的文章**: 163 篇  
  - gr-qc: 31 篇  
  - astro-ph: 111 篇  
**引力波相关**: 20 篇  
**提交类型**: 🆕 8 New • 🔄 2 Cross-lists • 🔄 10 Replacements  

## 1. pespace: A new tool of GPU-accelerated and auto-differentiable response generation and likelihood evaluation for space-borne gravitational wave detectors

**arXiv**: [2602.12011](https://arxiv.org/abs/2602.12011)  
**Authors**: Rui Niu, Chang Feng, Wen Zhao  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, astro-ph.IM  
**Type**: new submission  

**Abstract**: pespace: A new tool of GPU-accelerated and auto-differentiable response generation and likelihood evaluation for space-borne gravitational wave detectors Rui Niu, Chang Feng, Wen Zhao General Relativity and Quantum Cosmology (gr-qc); Instrumentation and Methods for Astrophysics (astro-ph.IM) Space-borne gravitational wave detectors will expand the scope of gravitational wave astronomy to the milli-Hertz band in the near future. The development of data analysis software infrastructure at the current stage is crucial. In this paper, we introduce \texttt{pespace} which can be used for the full Bayesian parameter estimation of massive black hole binaries with detectors including LISA, Taiji, and Tianqin. The core computations are implemented using the high-performance parallel programming framework \texttt{taichi-lang} which enables automatic differentiation and hardware acceleration across different architectures. We also reimplement the waveform models \texttt{PhenomXAS} and \texttt{PhenomXHM} in the separate package \texttt{tiwave} to integrate waveform generation within the \texttt{taichi-lang} scope, making the entire computation accelerated and differentiable. To demonstrate the functionality of the tool, we use a typical signal from a massive black hole binary to perform the full Bayesian parameter estimation with the complete likelihood function for three scenarios: including a single detector using the waveform with only the dominant mode; a single detector using the waveform including higher modes; and a detector network with higher modes included. The results demonstrate that higher modes are essential in breaking degeneracies, and coincident observations by the detector network can significantly improve the measurement of source properties. Additionally, automatic differentiation provides an accurate way to obtain the Fisher matrix without manual fine-tuning of the finite difference step size. Using a subset of extrinsic parameters, we show that the approximated posteriors obtained by the Fisher matrix agree well with those derived from Bayesian parameter estimation.  

---

## 2. Dark matter distributions around extreme mass ratio inspirals: effects of radial pressure and relativistic treatment

**arXiv**: [2602.12022](https://arxiv.org/abs/2602.12022)  
**Authors**: Yang Zhao, Yungui Gong  
**Date**: 16 Feb 2026  
**Categories**: gr-qc  
**Type**: new submission  

**Abstract**: Dark matter distributions around extreme mass ratio inspirals: effects of radial pressure and relativistic treatment Yang Zhao, Yungui Gong General Relativity and Quantum Cosmology (gr-qc) We investigate different treatments of dark matter (DM) distributions surrounding extreme mass ratio inspirals (EMRIs) to assess their impact on orbital evolution and gravitational wave emission. Density profiles derived from the mass current and from the energy-momentum tensor using a distribution function yield consistent results, but both differ substantially from profiles obtained using an anisotropic fluid model based on Einstein cluster ansatz. We find that the inclusion of radial pressure significantly modifies both the orbital dynamics and the resulting gravitational wave waveforms. By analyzing waveform dephasing and mismatches, we show that a fully relativistic treatment of DM distributions can substantially alter the detectability thresholds of DM halos. Our results demonstrate that radial pressure and relativistic modeling of DM are essential for accurately describing the dynamics and observational signatures of EMRIs embedded in DM halos.  

---

## 3. Black Holes Trapped by Ghosts

**arXiv**: [2602.12101](https://arxiv.org/abs/2602.12101)  
**Authors**: Cheng-Yong Zhang, Yunqi Liu, Bin Wang  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, hep-ph  
**Type**: new submission  

**Abstract**: Cheng-Yong Zhang, Yunqi Liu, Bin Wang General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph) Violent cosmic events, from black hole mergers to stellar collapses, often leave behind highly excited black hole remnants that inevitably relax to equilibrium. The prevailing view, developed over decades, holds that this relaxation is rapidly filtered into a linear regime, establishing linear perturbation theory as the bedrock of black hole spectroscopy and a key pillar of gravitational-wave physics. Here we unveil a distinct nonlinear regime that transcends the traditional paradigm: before the familiar linear ringdown, an intrinsically nonlinear, long-lived bottleneck can dominate the evolution. This stage is controlled by a saddle-node ghost in phase space, which traps the remnant and delays the onset of linearity by a timescale obeying a universal power-law. The ghost imprints a distinctive quiescence-burst signature on the emitted radiation: a prolonged silence followed by a violent burst and a delayed ringdown. Rooted in the bifurcation topology, it extends naturally to neutron and boson stars, echoing a topological universality shared with diverse nonlinear systems in nature. Our results expose a missing nonlinear chapter in gravitational dynamics and identify ghost-induced quiescence-burst patterns as clear targets for future observations.  

---

## 4. Measurement prospects for the pair-instability mass cutoff with gravitational waves

**arXiv**: [2602.11282](https://arxiv.org/abs/2602.11282)  
**Authors**: Matthew Mould, Jack Heinzel, Sofia Alvarez-Lopez, Cailin Plunkett, Noah E. Wolfe, Salvatore Vitale  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.HE, astro-ph.CO, astro-ph.IM, astro-ph.SR, gr-qc  
**Type**: cross-list from astro-ph.HE  

**Abstract**: Measurement prospects for the pair-instability mass cutoff with gravitational waves Matthew Mould, Jack Heinzel, Sofia Alvarez-Lopez, Cailin Plunkett, Noah E. Wolfe, Salvatore Vitale High Energy Astrophysical Phenomena (astro-ph.HE); Cosmology and Nongalactic Astrophysics (astro-ph.CO); Instrumentation and Methods for Astrophysics (astro-ph.IM); Solar and Stellar Astrophysics (astro-ph.SR); General Relativity and Quantum Cosmology (gr-qc) Pair-instability supernovae leave behind no compact remnants, resulting in a predicted gap in the distribution of stellar black-hole masses. Gravitational waves from binary black-hole mergers probe the relevant mass range and analyses of the LIGO-Virgo-KAGRA catalog (GWTC-4) indicate a possible mass cutoff at $40$-$50M_\odot$. However, the robustness of this result is yet to be tested. To this end, we simulate a comprehensive suite of gravitational-wave catalogs with full Bayesian parameter estimation and analyze them with parametric population models. For catalogs similar to GWTC-4, confident identification of a cutoff is not guaranteed, but GWTC-4 results are compatible with the best constraints among our simulations. Conversely, spurious false identification of a cutoff is unlikely. For catalogs expected by the end of the O4 observing run, uncertainty in the cutoff mass is reduced by $\gtrsim20\%$, but a cutoff at $40$-$50M_\odot$ yields only a lower bound on the $^{12}\mathrm{C}(\alpha,\gamma)^{16}\mathrm{O}$ reaction rate, which in terms of the S-factor at $300\,\mathrm{keV}$ may be $S_{300}\gtrsim125\,\mathrm{keV}\,\mathrm{b}$ at $90\%$ credibility by the end of O4. Relative uncertainties on the Hubble parameter $H_0$ from gravitational-wave data alone can still be up to $100\%$. We also analyze GWTC-4 with the nonparametric PixelPop population model, finding that some mass features are more prominent than in parametric models but a sharp cutoff is not required. However, the parametric model passes a likelihood-based predictive test in GWTC-4 and the PixelPop results are consistent with those from our simulated catalogs where a cutoff is present. We use the simple focus of this study to emphasize that such tests are necessary to make astrophysical claims from gravitational-wave catalogs going forward.  

---

## 5. The Dark Side of the Moon: Listening to Scalar-Induced Gravitational Waves

**arXiv**: [2602.12252](https://arxiv.org/abs/2602.12252)  
**Authors**: D. Blas, J. W. Foster, Y. Gouttenoire, A. J. Iovino, I. Musco, S. Trifinopoulos, M. Vanvlasselaer  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.CO, gr-qc, hep-ph  
**Type**: cross-list from astro-ph.CO  

**Abstract**: The Dark Side of the Moon: Listening to Scalar-Induced Gravitational Waves D. Blas, J. W. Foster, Y. Gouttenoire, A. J. Iovino, I. Musco, S. Trifinopoulos, M. Vanvlasselaer 8 pages, 4 figures, 1 appendix with 1 additional figures Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Phenomenology (hep-ph) The collapse of large-amplitude primordial curvature perturbations into planetary-mass primordial black holes generates a scalar-induced gravitational wave background in the $\mu $Hz frequency range that may be detectable by future Lunar Laser Ranging and Satellite Laser Ranging data. We derive projected constraints on the primordial black hole population from a null detection of stochastic gravitational wave background by these experiments, including the impact of the electroweak phase transition on the abundance of planetary-mass primordial black holes. We also discuss the connection between the obtained projected constraints and the recent microlensing observations by the HSC collaboration of the Andromeda Galaxy.  

---

## 6. Effect of ultralight dark matter on compact binary mergers

**arXiv**: [2503.19660](https://arxiv.org/abs/2503.19660)  
**Authors**: Kabir Chakravarti, Soham Acharya, Sumanta Chakraborty, Sudipta Sarkar  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, astro-ph.GA, hep-th  
**Type**: replaced  

**Abstract**: Effect of ultralight dark matter on compact binary mergers Kabir Chakravarti, Soham Acharya, Sumanta Chakraborty, Sudipta Sarkar 1. 13 pages, 5 figures 2. Improved binary evolution modelling. 3. Extended IMF analysis 4. Minor corrections and clarifications General Relativity and Quantum Cosmology (gr-qc); Astrophysics of Galaxies (astro-ph.GA); High Energy Physics - Theory (hep-th) The growing catalogue of gravitational wave events enables a statistical analysis of compact binary mergers, typically quantified by the merger rate density. This quantity can be influenced by ambient factors, following which, in this work we have investigated the impact of dark matter environment on the merger statistics. We construct a baseline astrophysical model of compact binary mergers and extend it by incorporating a model of ultra light dark matter, which affects the orbital evolution of binaries through accretion and dynamical friction. Our analysis of the merged population of binary progenitors demonstrates that, compared to the baseline model, ULDM can significantly alter the merger statistics when its ambient density becomes larger than 104GeV/cm3. A comparison with the gravitational wave data from the GWTC-3 catalogue provides insight into potential observational signatures of the ULDM in merger events, leading to possible constraints on the existence and density of dark matter distribution in galaxies.  

---

## 7. Spatially covariant gravity with two degrees of freedom in the presence of an auxiliary scalar field: Hamiltonian analysis

**arXiv**: [2508.02466](https://arxiv.org/abs/2508.02466)  
**Authors**: Jun-Cheng Zhu, Shu-Yu Li, Xian Gao  
**Date**: 16 Feb 2026  
**Categories**: gr-qc  
**Type**: replaced  

**Abstract**: Spatially covariant gravity with two degrees of freedom in the presence of an auxiliary scalar field: Hamiltonian analysis Jun-Cheng Zhu, Shu-Yu Li, Xian Gao 20 pages, no figure; v2 match CPC version Chinese Physics C Vol. 50, No. 3 (2026) 035105 General Relativity and Quantum Cosmology (gr-qc) A class of gravity theories respecting spatial covariance and in the presence of non-dynamical auxiliary scalar fields with only spatial derivatives is investigated. Generally, without higher temporal derivatives in the metric sector, there are 3 degrees of freedom (DOFs) propagating due to the breaking of general covariance. Through a Hamiltonian constraint analysis, we examine the conditions to eliminate the scalar DOF such that only 2 DOFs, which correspond the tensorial gravitational waves in a homogeneous and isotropic background, are propagating. We find that two conditions are needed, each of which can eliminate half degree of freedom. The second condition can be further classified into two cases according to its effect on the Dirac matrix. We also apply the formal conditions to a polynomial-type Lagrangian as a concrete example, in which all the monomials are spatially covariant scalars containing two derivatives. Our results are consistent with the previous analysis based on the perturbative method.  

---

## 8. Scalar-induced gravitational waves in spatially covariant gravity

**arXiv**: [2508.20000](https://arxiv.org/abs/2508.20000)  
**Authors**: Jiehao Jiang, Jieming Lin, Xian Gao  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, astro-ph.CO  
**Type**: replaced  

**Abstract**: Scalar-induced gravitational waves in spatially covariant gravity Jiehao Jiang, Jieming Lin, Xian Gao 26 pages, 8 figures; v2, match the EPJC version General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO) We investigate scalar-induced gravitational waves (SIGWs) in the framework of spatially covariant gravity (SCG), a broad class of Lorentz-violating modified gravity theories respecting only spatial diffeomorphism invariance. Extending earlier SCG formulations, we compute the general kernel function for SIGWs on a flat Friedmann-Lemaître-Robertson-Walker background, focusing on polynomial-type SCG Lagrangians up to $d=3$, where $d$ denotes the total number of derivatives in each monomial. We derive explicit expressions for the kernel in the case of power-law time evolution of the coefficients, and restrict attention to the subset of SCG operators whose tensor modes propagate at the speed of light, thereby avoiding late-time divergences in the fractional energy density of SIGWs. Instead of the usual Newtonian gauge, the breaking of time reparametrization symmetry in SCG necessitates a unitary gauge analysis. We compute the energy density of SIGWs for representative parameter combinations, finding distinctive deviations from general relativity (GR), including scale-dependent modifications to both the amplitude and the spectral shape. Our results highlight the potential of stochastic GW background measurements to probe spatially covariant gravity and other Lorentz-violating extensions of GR.  

---

## 9. Quantum reference frames for spacetime symmetries and large gauge transformations

**arXiv**: [2509.01458](https://arxiv.org/abs/2509.01458)  
**Authors**: Daan W. Janssen  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, math-ph  
**Type**: replaced  

**Abstract**: Quantum reference frames for spacetime symmetries and large gauge transformations Daan W. Janssen 5pp. Accepted as contribution to the proceedings of The 24th International Conference on General Relativity and Gravitation (GR24) and the 16th Edoardo Amaldi Conference on Gravitational Waves (Amaldi16), based on a talk given in session D4. v2: Corrected a typo in Eq. (2) General Relativity and Quantum Cosmology (gr-qc); Mathematical Physics (math-ph) Symmetries are a central concept in our understanding of physics. In quantum theories, a quantum reference frame (QRF) can be used to distinguish between observables related by a symmetry. The framework of operational QRFs provides a means to describe observables in terms of their relation to a reference quantum system. We discuss a number of applications of QRFs in the context of quantum field theory on curved spacetimes: 1) A type reduction result for algebras arising from QFTs and QRFs with good thermal properties. 2) Quantisation of boundary electric fluxes and gluing procedures for quantum electromagnetism on spacetimes with boundaries.  

---

## 10. Globally defined Carroll symmetry of gravitational waves

**arXiv**: [2510.16762](https://arxiv.org/abs/2510.16762)  
**Authors**: Mahmut Elbistan, Peng-Ming Zhang, Peter Horvathy  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, hep-th, math-ph  
**Type**: replaced  

**Abstract**: Globally defined Carroll symmetry of gravitational waves Mahmut Elbistan, Peng-Ming Zhang, Peter Horvathy Extended version. 22 pages, 11 figures. Further explanations and several new references added General Relativity and Quantum Cosmology (gr-qc); High Energy Physics - Theory (hep-th); Mathematical Physics (math-ph) The local Carroll symmetry of a gravitational wave found in Baldwin-Jeffery-Rosen coordinates is extended to a globally defined one by switching to Brinkmann coordinates. Two independent globally defined solutions of a Sturm-Liouville equation allow us to describe both the symmetries (translations and Carroll boosts) and the geodesic motions. One of them satisfies particular initial conditions which imply zero initial momentum, while the other does not. Pure displacement arises when the latter is turned off by requiring the momentum to vanish and when the wave parameters take, in addition, some particular values which correspond to having an integer half-wave number. The relation to the Schwarzian derivative is highlighted. We illustrate our general statements by the Pöschl-Teller profile.  

---

## 11. Hierarchical modeling of gravitational-wave populations for disentangling environmental and modified-gravity effects

**arXiv**: [2510.17398](https://arxiv.org/abs/2510.17398)  
**Authors**: Shubham Kejriwal, Enrico Barausse, Alvin J. K. Chua  
**Date**: 16 Feb 2026  
**Categories**: gr-qc, astro-ph.CO  
**Type**: replaced  

**Abstract**: Hierarchical modeling of gravitational-wave populations for disentangling environmental and modified-gravity effects Shubham Kejriwal, Enrico Barausse, Alvin J. K. Chua 11 + 7 pages, 6 figures; before proofs accepted General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO) The upcoming Laser Interferometer Space Antenna (LISA) will detect up to thousands of extreme-mass-ratio inspirals (EMRIs). These sources will spend $\sim 10^5$ cycles in band, and are therefore sensitive to tiny changes in the general-relativistic dynamics, potentially induced by astrophysical environments or modifications of general relativity (GR). Previous studies have shown that these effects can be highly degenerate for a single source. However, it may be possible to distinguish between them at the population level, because environmental effects should impact only a fraction of the sources, while modifications of GR would affect all. We therefore introduce a population-based hierarchical framework to disentangle the two hypotheses. Using simulated EMRI populations, we perform tests of the null vacuum-GR hypothesis and two alternative beyond-vacuum-GR hypotheses, namely migration torques (environmental effects) and time-varying $G$ (modified gravity). We find that with as few as $\approx 20$ detected sources, our framework can statistically distinguish between these three hypotheses, and even indicate if both environmental and modified gravity effects are simultaneously present in the population. Our framework can be applied to other models of beyond-vacuum-GR effects available in the literature.  

---

## 12. Gravitational wave oscillations in Multi-Proca dark energy models

**arXiv**: [2512.17088](https://arxiv.org/abs/2512.17088)  
**Authors**: Gabriel Gomez, Jose F. Rodriguez  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.CO, gr-qc  
**Type**: replaced  

**Abstract**: Gravitational wave oscillations in Multi-Proca dark energy models Gabriel Gomez, Jose F. Rodriguez Accepted for publication in JCAP. Matches the accepted version Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc) Gravitational wave oscillations arise from the exchange of energy between the metric perturbations and additional tensor modes. This phenomenon can occur even when the extra degrees of freedom consist of a triplet of massive Abelian vector fields, as in Multi-Proca dark energy models. In this work, we study gravitational wave oscillations in this class of models minimally coupled to gravity with a general potential, allowing also for a kinetic coupling between the vector field and dark matter that can, in principle, enhance the modulation of gravitational wave amplitudes. After consistently solving the background dynamics, requiring the model parameters to reproduce a phase of late-time accelerated expansion, we assess the accuracy of commonly used analytical approximations and quantify the impact of gravitational wave amplitude modulation for current detectors (LIGO--Virgo) and future missions such as LISA. Although oscillations are present in these scenarios, we find that the effective mass scale (the mixing mass) governing the phenomenon is $m_g \sim \mu_A$, where $\mu_A$ is the (time-dependent) effective mass of the vector dark-energy field. Detectability of gravitational wave oscillations, however, requires $m_g \gg H_0$, which is in tension with the ultra-light masses typically needed to drive accelerated expansion $\mu_A \sim H_0 \sim 10^{-33}\,\mathrm{eV}$. Therefore, if gravitational wave oscillations were to be detected at the corresponding frequencies, they could not be attributed to these classes of dark-energy models.  

---

## 13. Forecasting Constraints on Cosmology and Modified Gravitational-wave Propagation by Strongly Lensed Gravitational Waves Associating with Galaxy Surveys

**arXiv**: [2601.21820](https://arxiv.org/abs/2601.21820)  
**Authors**: Anson Chen, Jun Zhang  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.CO, gr-qc  
**Type**: replaced  

**Abstract**: Forecasting Constraints on Cosmology and Modified Gravitational-wave Propagation by Strongly Lensed Gravitational Waves Associating with Galaxy Surveys Anson Chen, Jun Zhang Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc) Gravitational lensing of gravitational wave (GW) will become the next frontier in studying cosmology and gravity. While time-delay cosmography using quadruply lensed GW events associated with optical images of the lens systems can provide precise measurement of the Hubble constant ($H_0$), they are considered to be much rarer than doubly lensed events. In this work, we analyze time-delay cosmography with doubly lensed GW events for the first time. We generate mock doubly lensed GW events with designed sensitivity of the LIGO-Virgo-KAGRA (LVK) O5 network, with LIGO post-O5 upgrade, and with Einstein Telescope (ET) + Cosmic Explorer (CE) respectively, and select the events that can be associated with future galaxy surveys. Over 1000 realizations, we find an average of 0.2(2.4) qualified events with the LVK O5(post-O5) network. Whereas with the ET+CE network, we find an average of 73.2 qualified events over 100 realizations. Using the Singular Isothermal Sphere (SIS) lens model, we jointly estimate waveform parameters and the impact parameter with doubly lensed GW signals, and then forecast the constraints on cosmological parameters and modified GW propagation by combining time-delay cosmography and the standard siren approach. The average posterior gives a constraint on $H_0$ with a relative uncertainty of $14\%$, $10\%$ and $0.42\%$ in the $\Lambda$CDM model for the LVK O5, LVK post-O5, and ET+CE network, respectively. While the LVK network gives uninformative constraints on the $(w_0,w_a)$ dynamical dark energy model, the ET+CE network yields a moderate constraint of $w_0=-1.02^{+0.31}_{-0.22}$ and $w_a=0.48^{+0.99}_{-1.54}$. In addition, our method can provide precise constraints on modified GW propagation effects jointly with $H_0$.  

---

## 14. Stone Skipping Black Holes in Ultralight Dark Matter Solitons

**arXiv**: [2602.11512](https://arxiv.org/abs/2602.11512)  
**Authors**: Alan Zhang, Yourong Wang, J. Luna Zagorac, Richard Easther  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.CO, astro-ph.GA  
**Type**: new submission  

**Abstract**: Stone Skipping Black Holes in Ultralight Dark Matter Solitons Alan Zhang, Yourong Wang, J. Luna Zagorac, Richard Easther Cosmology and Nongalactic Astrophysics (astro-ph.CO); Astrophysics of Galaxies (astro-ph.GA) The orbit of a black hole moving within an ultralight dark matter (ULDM) soliton is naively expected to decay due to dynamical friction. However, single black holes can undergo ``stone skipping'', with their orbital radius varying quasi-periodically. We show that stone skipping is induced by the dipole excitation of the soliton. We model it as resonance in a forced, damped harmonic oscillator, demonstrating that the coherent response of the soliton can significantly modify the dynamics of objects orbiting within it. This suggests that a dipole perturbation of a soliton can modify inspiral timescales if the black holes masses are significantly less than the soliton mass, with implications for supermassive black hole dynamics, the final parsec problem and gravitational wave observations in a ULDM cosmology.  

---

## 15. Searching for Anisotropy in the Gravitational Wave Background Using the Parkes Pulsar Timing Array

**arXiv**: [2602.11529](https://arxiv.org/abs/2602.11529)  
**Authors**: Yiqin Chen, Shi-Yi Zhao, Zhi-Zhang Peng, Xingjiang Zhu, N. D. Ramesh Bhat, Zu-Cheng Chen, Małgorzata Curyło, Valentina Di Marco, George Hobbs, Agastya Kapur, Wenhua Ling, Rami Mandow, Saurav Mishra, Daniel J. Reardon, Christopher J. Russell, Ryan M. Shannon, Jacob Cardinal Tremblay, Jingbo Wang, Lei Zhang, Andrew Zic  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: Searching for Anisotropy in the Gravitational Wave Background Using the Parkes Pulsar Timing Array Yiqin Chen, Shi-Yi Zhao, Zhi-Zhang Peng, Xingjiang Zhu, N. D. Ramesh Bhat, Zu-Cheng Chen, Małgorzata Curyło, Valentina Di Marco, George Hobbs, Agastya Kapur, Wenhua Ling, Rami Mandow, Saurav Mishra, Daniel J. Reardon, Christopher J. Russell, Ryan M. Shannon, Jacob Cardinal Tremblay, Jingbo Wang, Lei Zhang, Andrew Zic Accepted for publication in Physical Review D. 11 pages, 5 figures High Energy Astrophysical Phenomena (astro-ph.HE) In recent years, several pulsar timing array collaborations have reported evidence for a nanohertz gravitational wave background (GWB). Such a background signal could be produced by supermassive binary black holes, early-Universe processes such as inflation and phase transitions, or a mixture of both. One way to disentangle different contributions to the GWB is to search for anisotropic signatures. In this work, we search for anisotropy in the GWB using the third data release of the Parkes Pulsar Timing Array. Our analysis employs both the radiometer method and the spherical harmonic basis to characterize the distribution of GWB power across the sky. We calculate the angular power in the lowest five frequency bins and compare it with detection thresholds determined under the null hypothesis of isotropy. In the 5.26 nHz frequency bin, we identify a hotspot in the reconstructed sky map with a $p$-value of $0.016$ (the lowest in our analysis), which we attribute to noise fluctuations. While our search reveals no statistically significant anisotropy, we expect that the precise measurement of angular power spectrum of the GWB will become instrumental in determining the origin of the nanohertz GWB signal.  

---

## 16. Population synthesis predictions of the Galactic compact binary gravitational wave foreground detectable by LISA

**arXiv**: [2602.11765](https://arxiv.org/abs/2602.11765)  
**Authors**: Jake McMillan , Adam Ingram , Cordelia Dashwood Brown , Andrei Igoshev , Matthew Middleton , Grzegorz Wiktorowicz , Simone Scaringi School of Mathematics, Statistics, and Physics, Newcastle University, Centre for Advanced Instrumentation, Department of Physics, Durham University, School of Physics and Astronomy, University of Southampton, Nicolaus Copernicus Astronomical Center, Polish Academy of Sciences, Centre for Extragalactic Astronomy, Department of Physics, Durham University, INAF - Osservatorio Astronomico di Capodimonte)  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: Population synthesis predictions of the Galactic compact binary gravitational wave foreground detectable by LISA Jake McMillan (1 and 2), Adam Ingram (1), Cordelia Dashwood Brown (3), Andrei Igoshev (1), Matthew Middleton (3), Grzegorz Wiktorowicz (4), Simone Scaringi (5 and 6) ((1) School of Mathematics, Statistics, and Physics, Newcastle University, (2) Centre for Advanced Instrumentation, Department of Physics, Durham University, (3) School of Physics and Astronomy, University of Southampton, (4) Nicolaus Copernicus Astronomical Center, Polish Academy of Sciences, (5) Centre for Extragalactic Astronomy, Department of Physics, Durham University, (6) INAF - Osservatorio Astronomico di Capodimonte) High Energy Astrophysical Phenomena (astro-ph.HE) We use population synthesis modelling to predict the gravitational wave (GW) signal that the Laser Interferometer Space Antenna (LISA) will detect from the Galactic population of compact binary systems. We implement a realistic star formation history with time and position-dependent metallicity, and account for the effect of supernova kicks on present-day positions. We consider all binaries that have a white dwarf (WD), neutron star (NS), or black hole primary in the present-day. We predict that the summed GW signal from all Galactic binaries will already be detectable 3 months into the LISA mission, by measuring the power spectrum of the total GW strain. We provide a simple publicly available code to calculate such a power spectrum from a user-defined binary population. In the full 4 year baseline mission lifetime, we conservatively predict that $>2000$ binaries could be individually detectable as GW sources. We vary the assumed common envelope (CE) efficiency $\alpha$, and find that it influences both the shape of the power spectrum and the relative number of detectable systems with WD and NS progenitors. In particular, the ratio of individually detectable binaries with chirp mass $\mathcal{M} < M_\odot$ to those with $\mathcal{M} \geqslant M_\odot$ increases with $\alpha$. We therefore conclude that LISA may be able to diagnose the CE efficiency, which is currently poorly constrained.  

---

## 17. Impact of crust-core connection procedures on the tidal deformability of neutron stars

**arXiv**: [2602.11809](https://arxiv.org/abs/2602.11809)  
**Authors**: Junbo Pang, Hong Shen, Jinniu Hu  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: Impact of crust-core connection procedures on the tidal deformability of neutron stars Junbo Pang, Hong Shen, Jinniu Hu 14 pages, 10 figures, 3 tables, has been accepted by Physical Review C High Energy Astrophysical Phenomena (astro-ph.HE) We study the impact of crust-core connection procedures on various neutron-star properties, especially on the tidal deformability. We consider three types of connection procedures to treat the discontinuity in a nonunified equation of state around the crust-core transition: (1) the direct connection procedure, (2) the crossover connection procedure, and (3) the segmented method. Our results indicate that the mass-radius relations of neutron stars are almost unaffected by the details of the connection procedure. However, the tidal deformabilities of neutron stars are sensitive to the crust-core connection procedures. The tidal deformability is closely related to gravitational-wave measurements. For a canonical 1.4$M_\odot$ neutron star, uncertainties in the tidal deformability $\Lambda_{1.4}$ from different connection procedures can exceed 20\%. We find that the direct connection procedure yields significantly larger uncertainties in the tidal deformability, while the segmented method and crossover connection procedure provide relatively stable results.  

---

## 18. Long-Term Multidimensional Models of Core-Collapse Supernovae: Progress and Challenges

**arXiv**: [2502.14836](https://arxiv.org/abs/2502.14836)  
**Authors**: H.-Thomas Janka  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.HE, hep-ph, nucl-th  
**Type**: replaced  

**Abstract**: Long-Term Multidimensional Models of Core-Collapse Supernovae: Progress and Challenges H.-Thomas Janka (MPI Astrophysics, Garching) 40 pages, 8 figures; minor revisions due to referee comments; Annual Review of Nuclear and Particle Science 75, 425 (2025), article DOI: this https URL errors in Fig.8d corrected, new version consistent with arXiv:2602.02651 High Energy Astrophysical Phenomena (astro-ph.HE); High Energy Physics - Phenomenology (hep-ph); Nuclear Theory (nucl-th) Self-consistent, multidimensional core-collapse supernova (SN) simulations, especially in 3D, have achieved tremendous progress over the past 10 years. They are now able to follow the entire evolution from core collapse through bounce, neutrino-triggered shock revival, shock breakout at the stellar surface to the electromagnetic SN outburst and the subsequent SN remnant phase. Thus they provide general support for the neutrino-driven explosion mechanism by reproducing observed SN energies, neutron-star (NS) kicks, and diagnostically relevant radioactive isotope yields; they allow to predict neutrino and gravitational-wave signals for many seconds of proto-NS cooling; they confirm correlations between explosion and progenitor or remnant properties already expected from previous spherically symmetric (1D) and 2D models; and they carve out various scenarios for stellar-mass black-hole (BH) formation. Despite these successes it is currently unclear which stars explode or form BHs, because different modeling approaches disagree and suggest the possible importance of the 3D nature of the progenitors and of magnetic fields. The role of neutrino flavor conversion in SN cores still needs to be better understood, the nuclear equation of state including potential phase transitions implies major uncertainties, the SN 1987A neutrino measurements raise new puzzles, and tracing a possible correlation of NS spins and kicks requires still more refined SN simulations.  

---

## 19. Are NICER and GW170817 constraints suggesting a compactified scenario for Neutron stars?

**arXiv**: [2512.24729](https://arxiv.org/abs/2512.24729)  
**Authors**: Asim Kumar Saha, Tuhin Malik, Ritam Mallick  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.HE  
**Type**: replaced  

**Abstract**: Are NICER and GW170817 constraints suggesting a compactified scenario for Neutron stars? Asim Kumar Saha, Tuhin Malik, Ritam Mallick 14 pages, 6 Figures and 3 Tables High Energy Astrophysical Phenomena (astro-ph.HE) Astrophysical observations from NICER and gravitational wave data constrain the properties of matter at the cores of neutron stars, enabling us to probe high-density matter with greater accuracy. To understand its implications for neutron stars, three distinct class-agnostic equation-of-state ensembles are constructed using the speed-of-sound parametrisation, which can describe matter in neutron-star cores. Bayesian analysis is employed to constrain the parameters, namely, the squared speed of sound and chemical potential, using the observational data. The Bayesian inference shows that the observations effectively constrain the low-density region of the equation of state. The astrophysical bound favours a softer, low-density equation of state in which the phase transition occurs at intermediate densities, thereby reducing the upper mass bounds for neutron stars. For the equation of state with density discontinuity, the discontinuities are preferably small. The equation of state with maximum mass configuration shows considerable stiffening from very low density, providing pressure support to generate maximum mass. In contrast, the equation of state with the maximum compact stellar configuration has a softer low-density equation of state, followed by pronounced stiffening, yielding the maximum compact configuration. The observationally favoured EoS shares the same qualitative structure as the maximum-compactness EoS: relative softness at intermediate densities transitioning to stiffness at high densities, a configuration gravity naturally favours.  

---

## 20. Design and characterization of W-band and D-band calibration sources for the AliCPT-1 experiment

**arXiv**: [2602.11620](https://arxiv.org/abs/2602.11620)  
**Authors**: Xu-Fang Li, Cong-Zhan Liu, Ai-Mei Zhang, Zheng-Wei Li, Xue-Feng Lu, Zhong-Xue Xin, Guo-Feng Wang, Yong-Ping Li, Yong-Jie Zhang, Shi-Bo Shu, Yi-Fei Zhang, Ya-Qiong Li, Zhi Chang, Dai-Kang Yan  
**Date**: 16 Feb 2026  
**Categories**: astro-ph.IM  
**Type**: new submission  

**Abstract**: Design and characterization of W-band and D-band calibration sources for the AliCPT-1 experiment Xu-Fang Li, Cong-Zhan Liu, Ai-Mei Zhang, Zheng-Wei Li, Xue-Feng Lu, Zhong-Xue Xin, Guo-Feng Wang, Yong-Ping Li, Yong-Jie Zhang, Shi-Bo Shu, Yi-Fei Zhang, Ya-Qiong Li, Zhi Chang, Dai-Kang Yan Journal of Astronomical Telescopes,Instruments, and Systems, 2026, Vol. 12 Instrumentation and Methods for Astrophysics (astro-ph.IM) Ali Cosmic Microwave Background Polarization Telescope (AliCPT-1) is the first Chinese cosmic microwave background experiment aiming to make sensitive polarization maps of the potential B-mode signal from inflationary gravitational waves. The telescope was deployed on the Tibet Ali site at 5250 m above sea level in early 2025. Before and after each observation season, the instrument performance must be carefully calibrated, including the far field beam performance, far sidelobe, spectral response, polarization angle, and cross-polar beam response. To characterize these optical performances, several calibrators have been developed. We developed a W-band source and a D-band source for the AliCPT-1 telescope's beam characterizations. We present the design and performance of the two calibration sources.  

---

