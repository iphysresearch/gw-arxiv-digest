# Complete Daily GW arXiv Digest - 2025-09-18

**总爬取文章**: 190 篇  
**今天的文章**: 190 篇  
  - gr-qc: 40 篇  
  - astro-ph: 122 篇  
**引力波相关**: 26 篇  
**提交类型**: 🆕 12 New • 🔄 7 Cross-lists • 🔄 7 Replacements  

## 1. Random Forest Classification of MBTA Gravitational-Wave Triggers for Low-Latency Detection

**arXiv**: [2509.12882](https://arxiv.org/abs/2509.12882)  
**Authors**: Lorenzo Mobilia, Gianluca Maria Guidi  
**Date**: 18 Sep 2025  
**Categories**: gr-qc, astro-ph.IM  
**Type**: new submission  

**Abstract**: Random Forest Classification of MBTA Gravitational-Wave Triggers for Low-Latency Detection Lorenzo Mobilia, Gianluca Maria Guidi General Relativity and Quantum Cosmology (gr-qc); Instrumentation and Methods for Astrophysics (astro-ph.IM) In this work, we explore a possible application of a machine learning classifier for candidate events in a template-based search for gravitational-wave (GW) signals from various compact system sources. We analyze data from the O3a and O3b data acquisition campaign, during which the sensitivity of ground-based detectors is limited by real non-Gaussian noise transient. The state-of-the-art searches for such signals tipically rely on the signal-to-noise ratio (SNR) and a chi-square test to assess the consistency of the signal with an inspiral template. In addition, a combination of these and other statistical properties are used to build a 're-weighted SNR' statistics. We evaluate a Random Forest classifiers on a set of double-coincidence events identified using the MBTA pipeline. The new classifier achieves a modest but consistent increase in event detection at low false positive rates relative to the standard search. Using the output statistics from the Random Forest classifier, we compute the probability of astrophysical origin for each event, denoted as $p_\mathrm{astro}$. This is then evaluated for the events listed in existing catalogs, with results consistent with those from the standard search. Finally, we search for new possible candidates using this new statistics, with $p_\mathrm{astro} > 0.5$, obtaining a new subthreshold candidate (IFAR =0.05) event at $gps: 1240423628$ .  

---

## 2. Quantum Computing Tools for Fast Detection of Gravitational Waves in the Context of LISA Space Mission

**arXiv**: [2509.12929](https://arxiv.org/abs/2509.12929)  
**Authors**: Maria-Catalina Isfan, Laurentiu-Ioan Caramete, Ana Caramete, Daniel Tonoiu, Alexandru Nicolin-Zaczek  
**Date**: 18 Sep 2025  
**Categories**: gr-qc, astro-ph.CO, astro-ph.IM  
**Type**: new submission  

**Abstract**: Quantum Computing Tools for Fast Detection of Gravitational Waves in the Context of LISA Space Mission Maria-Catalina Isfan, Laurentiu-Ioan Caramete, Ana Caramete, Daniel Tonoiu, Alexandru Nicolin-Zaczek Submitted to Classical and Quantum Gravity General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO); Instrumentation and Methods for Astrophysics (astro-ph.IM); Data Analysis, Statistics and Probability (physics.data-an) The field of gravitational wave (GW) detection is progressing rapidly, with several next-generation observatories on the horizon, including LISA. GW data is challenging to analyze due to highly variable signals shaped by source properties and the presence of complex noise. These factors emphasize the need for robust, advanced analysis tools. In this context, we have initiated the development of a low-latency GW detection pipeline based on quantum neural networks (QNNs). Previously, we demonstrated that QNNs can recognize GWs simulated using post-Newtonian approximations in the Newtonian limit. We then extended this work using data from the LISA Consortium, training QNNs to distinguish between noisy GW signals and pure noise. Currently, we are evaluating performance on the Sangria LISA Data Challenge dataset and comparing it against classical methods. Our results show that QNNs can reliably distinguish GW signals embedded in noise, achieving classification accuracies above 98\%. Notably, our QNN identified 5 out of 6 mergers in the Sangria blind dataset. The remaining merger, characterized by the lowest amplitude, highlights an area for future improvement in model sensitivity. This can potentially be addressed using additional mock training datasets, which we are preparing, and by testing different QNN architectures and ansatzes.  

---

## 3. Classical and quantum aspects of perturbations in Primordial Universe

**arXiv**: [2509.13080](https://arxiv.org/abs/2509.13080)  
**Authors**: Alice Boldrin  
**Date**: 18 Sep 2025  
**Categories**: gr-qc  
**Type**: new submission  

**Abstract**: Classical and quantum aspects of perturbations in Primordial Universe Alice Boldrin 127 pages, 22 figures, submitted in fulfilment of the requirements for the degree of Doctor of Philosophy in Theoretical Physics at the Graduate School of the National Centre for Nuclear Research (NCBJ), Warsaw General Relativity and Quantum Cosmology (gr-qc) In this work, our aim is to obtain a Hamiltonian formulation suitable for canonical quantization. Moreover, we assume that the early Universe can be described with fewer initial symmetries, thus we abandon the isotropy assumption and instead explore anisotropic universes, beginning with the simplest one, namely Bianchi I (BI). The presence of small initial fluctuations in the early universe can be well described by perturbations around a homogeneous background. GR is a constrained system, and we apply the so-called Dirac procedure for constrained systems to derive a gauge-invariant Hamiltonian formulation suitable for quantization. In this work, we present how this procedure can be extended to a generic background and its relation to the Kuchar decomposition. Subsequently, we apply this formulation to a BI universe, obtaining new and interesting results on the gauge-invariant representation of matter and geometry perturbations. Contrary to the FLRW case, in which all the modes decouple, in BI we see that scalar and tensor modes do not decouple. We show that new types of gauge-fixing conditions exit in this case. For instance, a gravitational wave can be encoded into scalar modes, by introducing a new gauge which is not valid in FLRW. Furthermore, we make a first step towards a consistent and unified quantization of the composite system made of a background mode and perturbation modes. Specifically, we study tensor modes in a FLRW universe. We focus on the relation between the choice of internal time of the universe and the quantum evolution it undergoes. Our results indicate that the time reparametrization invariance in general relativity affects the quantum evolution of the background and perturbation modes. However, in the classical limit, i.e. for a large universe, the dynamics becomes unique. Thus, the predictive power of the theory is maintained.  

---

## 4. Short-Duration Gravitational Wave Burst Detection using Convolutional Neural Network

**arXiv**: [2509.13241](https://arxiv.org/abs/2509.13241)  
**Authors**: Matteo Pracchia, Sacha Peters, Maxime Fays  
**Date**: 18 Sep 2025  
**Categories**: gr-qc  
**Type**: new submission  

**Abstract**: Short-Duration Gravitational Wave Burst Detection using Convolutional Neural Network Matteo Pracchia, Sacha Peters, Maxime Fays General Relativity and Quantum Cosmology (gr-qc) Detecting unmodeled gravitational wave (GW) bursts presents significant challenges due to the lack of accurate waveform templates required for matched-filtering techniques. A primary difficulty lies in distinguishing genuine signals from transient noise. Machine learning approaches, particularly convolutional neural networks (CNNs), offer promising alternatives for this classification problem. This paper presents a CNN-based pipeline for detecting short GW bursts (duration $< 10~\mathrm{s}$), adapted from an existing framework designed for longer-duration events. The CNN has been trained on core-collapse supernova (CCSN) gravitational waveform models injected into simulated Gaussian noise. The network successfully identifies these signals and generalizes to CCSN waveforms not included in the training set, showing the potential of U-Net architectures for detecting short-duration gravitational wave transients across diverse astrophysical scenarios.  

---

## 5. Towards detecting the time perturbations from GWs in asynchronous gauges

**arXiv**: [2509.13321](https://arxiv.org/abs/2509.13321)  
**Authors**: Stefano Bondani, Sergio Luigi Cacciatori  
**Date**: 18 Sep 2025  
**Categories**: gr-qc  
**Type**: new submission  

**Abstract**: Towards detecting the time perturbations from GWs in asynchronous gauges Stefano Bondani, Sergio Luigi Cacciatori General Relativity and Quantum Cosmology (gr-qc) The experimental possibility of detecting gravitational waves via their induced time perturbations is explored here, expanding from previous work. The oscillations of the time-time component in the metric are made explicit when working in asynchronous gauges: the desynchronization between a perturbed clock and a reference unperturbed clock constitutes the corresponding observable core target of a detector. To this end we explore the experimental techniques currently available for a preliminary assessment towards a feasibility study. We survey the state of the art in the fields of high precision timing and information preservation, necessary for achieving geodesic non-locality. A synthesis for a feasible prototype detector with the desired characteristics is presented. The optimum point between existing technologies is found around the 1 Hz frequency band, opening the window for the observation of classes of speculated sources of gravitational radiation such as intermediate mass black hole binaries.  

---

## 6. Systematic Effects of Chaotic Magnetic Fields on Neutron Star Tidal Deformability: Implications for Gravitational Wave Constraints on Dense Matter

**arXiv**: [2509.12246](https://arxiv.org/abs/2509.12246)  
**Authors**: Debarshi Mukherjee  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.HE, gr-qc  
**Type**: cross-list from astro-ph.HE  

**Abstract**: Systematic Effects of Chaotic Magnetic Fields on Neutron Star Tidal Deformability: Implications for Gravitational Wave Constraints on Dense Matter Debarshi Mukherjee High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) We investigate the effects of strong magnetic fields on the equation of state (EoS) of neutron star matter and the resulting implications for tidal deformability measurements in binary neutron star (BNS) mergers. A critical issue with previous magnetized neutron star studies is the treatment of magnetic field anisotropy in the Tolman-Oppenheimer-Volkoff (TOV) equations. To address this fundamental problem, we employ the chaotic magnetic field approximation, which allows for a self-consistent treatment of magnetic pressure while maintaining isotropy. Using a relativistic mean field approach with properly implemented magnetic field corrections, we compute mass-radius relations and tidal deformability parameters for neutron stars with magnetic field strengths ranging from $10^{15}$ to $10^{16}$ G. Our systematic study reveals that magnetic fields induce increases in both stellar radii (0.8--2.3\%) and tidal deformabilities (4.2--18.1\%) compared to field-free cases, with effects scaling approximately as $B^{1/2}$. These modifications, while modest, are potentially detectable with current and next-generation gravitational wave detectors. For a canonical $1.4\,M_\odot$ neutron star, the tidal deformability increases from $\Lambda_{1.4} = 678 \times 10^6$ in the absence of magnetic fields to $\Lambda_{1.4} = 803 \times 10^6$ for $B = 10^{16}$ G. We demonstrate that magnetic field effects must be considered when constraining the neutron star equation of state using gravitational wave observations, particularly for populations including highly magnetized neutron stars. Our results suggest that the current GW170817 constraint on tidal deformability may require systematic corrections when accounting for magnetic field effects. We provide scaling relations for magnetic field corrections and discuss the implications for population studies of neutron star mergers with next-generation detectors.  

---

## 7. Probing the millisecond pulsar origin of the GeV excess in the Galactic Centre with LISA

**arXiv**: [2509.12998](https://arxiv.org/abs/2509.12998)  
**Authors**: Valeriya Korol, Andrei Igoshev  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.HE, astro-ph.CO, gr-qc  
**Type**: cross-list from astro-ph.HE  

**Abstract**: Probing the millisecond pulsar origin of the GeV excess in the Galactic Centre with LISA Valeriya Korol, Andrei Igoshev Submitted to A&A. Comments are welcome High Energy Astrophysical Phenomena (astro-ph.HE); Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc) The GeV $\gamma$-ray excess observed towards the Galactic Centre remains unexplained. While dark matter annihilation has long been considered a leading interpretation, an alternative scenario involving a large population of millisecond pulsars has not been ruled out. Testing this hypothesis with electromagnetic observations is difficult, as pulsar searches in the bulge are strongly affected by scattering, high sky temperature, and source confusion. We investigate whether gravitational-wave observations with the Laser Interferometer Space Antenna (LISA) could provide an independent probe of the millisecond pulsar binary population in the Galactic bulge. We construct synthetic populations of millisecond pulsar-white dwarf binaries under two illustrative formation scenarios: an accreted scenario, in which systems are deposited by disrupted globular clusters, and an in situ scenario, in which binaries form through isolated binary evolution. In both cases, only $10^{-5}$--$10^{-4}$ of the underlying bulge population is detectable by LISA. Nevertheless, even a few detections would imply tens to hundreds of thousands of unseen systems. Accreted binaries are expected to have lower chirp masses ($\sim$0.4 M$_\odot$), while in situ binaries produce more massive companions ($\sim$0.9 M$_\odot$). LISA will measure binary frequencies with high precision, but chirp masses can only be determined for the most massive or highest-frequency systems. Distinguishing millisecond pulsar binaries from the far more numerous double white dwarfs will be challenging, though LISA detections could provide valuable targets for follow-up with the Square Kilometre Array, enabling a critical test of the millisecond pulsar origin of the $\gamma$-ray excess.  

---

## 8. TESLA-X: An effective method to search for sub-threshold lensed gravitational waves with a targeted population model

**arXiv**: [2311.06416](https://arxiv.org/abs/2311.06416)  
**Authors**: Alvin K. Y. Li, Juno C.L. Chan, Heather Fong, Aidan H.Y. Chong, Alan J. Weinstein, Jose M. Ezquiaga  
**Date**: 18 Sep 2025  
**Categories**: gr-qc, astro-ph.IM  
**Type**: replaced  

**Abstract**: TESLA-X: An effective method to search for sub-threshold lensed gravitational waves with a targeted population model Alvin K. Y. Li, Juno C.L. Chan, Heather Fong, Aidan H.Y. Chong, Alan J. Weinstein, Jose M. Ezquiaga Mon Not R Astron Soc (2025) 998-1010 General Relativity and Quantum Cosmology (gr-qc); Instrumentation and Methods for Astrophysics (astro-ph.IM) Strong gravitational lensing can produce copies of gravitational-wave signals from the same source with the same waveform morphologies but different amplitudes and arrival times. Some of these strongly-lensed gravitational-wave signals can be demagnified and become subthreshold. We present TESLA-X, an enhanced approach to the original GstLAL-based TargetEd Subthreshold Lensing seArch (TESLA) method, for improving the detection efficiency of these potential subthreshold lensed signals. TESLA-X utilizes lensed injections to generate a targeted population model and a targeted template bank. We compare the performance of a full template bank search, TESLA, and TESLA-X methods via a simulation campaign, and demonstrate the performance of TESLA-X in recovering lensed injections, particularly targeting a mock event. Our results show that the TESLA-X method achieves a maximum of $\sim 10\%$ higher search sensitivity compared to the TESLA method within the subthreshold regime, presenting a step towards detecting the first lensed gravitational wave. TESLA-X will be employed for the LIGO-Virgo-KAGRA's collaboration-wide analysis to search for lensing signatures in the fourth observing run.  

---

## 9. Coherence DeepClean: Toward autonomous denoising of gravitational-wave detector data

**arXiv**: [2501.04883](https://arxiv.org/abs/2501.04883)  
**Authors**: Christina Reissel, Siddharth Soni, Muhammed Saleem, Michael Coughlin, Philip Harris, Erik Katsavounidis  
**Date**: 18 Sep 2025  
**Categories**: gr-qc, astro-ph.IM  
**Type**: replaced  

**Abstract**: Coherence DeepClean: Toward autonomous denoising of gravitational-wave detector data Christina Reissel, Siddharth Soni, Muhammed Saleem, Michael Coughlin, Philip Harris, Erik Katsavounidis General Relativity and Quantum Cosmology (gr-qc); Instrumentation and Methods for Astrophysics (astro-ph.IM) Technical and environmental noise in ground-based laser interferometers designed for gravitational-wave observations like Advanced LIGO, Advanced Virgo and KAGRA, can manifest as narrow (<1Hz) or broadband ($10'$s or even $100'$s of Hz) spectral lines and features in the instruments' strain amplitude spectral density. When the sources of this noise cannot be identified or removed, in cases where there are witness sensors sensitive to this noise source, denoising of the gravitational-wave strain channel can be performed in software, enabling recovery of instrument sensitivity over affected frequency bands. This noise hunting and removal process can be particularly challenging due to the wealth of auxiliary channels monitoring the interferometry and the environment and the non-linear couplings that may be present. In this work, we present a comprehensive analysis approach and corresponding cyberinfrastructure to promptly identify and remove noise in software using machine learning techniques. The approach builds on earlier work (referred to as DeepClean) in using machine learning methods for linear and non-linear regression of noise. We demonstrate how this procedure can be operated and optimized in a tandem fashion close to online data taking; it starts off with a coherence monitoring analysis that first singles out and prioritizes witness channels that can then be used by DeepClean. The resulting denoised strain by DeepClean reflects a 1.4\% improvement in the binary neutron star range, which can translate into a 4.3\% increase in the sensitive volume. This cyber infrastructure we refer to as Coherence DeepClean, or CDC, is a significant step toward autonomous operations of noise subtraction for ground-based interferometers.  

---

## 10. Artificial Precision Timing Array: bridging the decihertz gravitational-wave sensitivity gap with clock satellites

**arXiv**: [2401.13668](https://arxiv.org/abs/2401.13668)  
**Authors**: Lucas M. B. Alves, Andrew G. Sullivan, Xingyu Ji, Doğa Veske, Imre Bartos, Sebastian Will, Zsuzsa Márka, Szabolcs Márka  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.IM, astro-ph.HE, gr-qc  
**Type**: replaced  

**Abstract**: Artificial Precision Timing Array: bridging the decihertz gravitational-wave sensitivity gap with clock satellites Lucas M. B. Alves, Andrew G. Sullivan, Xingyu Ji, Doğa Veske, Imre Bartos, Sebastian Will, Zsuzsa Márka, Szabolcs Márka Instrumentation and Methods for Astrophysics (astro-ph.IM); High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) Gravitational-wave astronomy has developed enormously over the last decade with the first detections and continuous development across broad frequency bands. However, the decihertz range has largely been left out of this development. Gravitational waves in this band are emitted by some of the most enigmatic sources, including intermediate-mass binary black hole mergers, early inspiraling compact binaries$\unicode{x2014}$whose late evolution and merger are seen by Earth-based detectors$\unicode{x2014}$, and possibly primordial gravitational waves. To tap this exciting band, we propose the construction of a detector based on pulsar timing principles, the Artificial Precision Timing Array (APTA). We envision APTA as a solar system array of artificial ``pulsars''$\unicode{x2014}$precision-time-reference-carrying satellites that emit periodic electromagnetic signals towards Earth or other satellite constellation centrum. In this fundamental study, we estimate the clock precision needed for APTA to be able to detect gravitational waves. Our results suggest that 6 satellites and a clock relative uncertainty of $10^{-18}$ at 1 s of averaging, which is currently attainable with atomic clocks, would be sufficient for APTA to reach pristine sensitivity in the decihertz band and be sensitive to $10^3\unicode{x2013}10^4$ $\mathrm{M}_\odot$ black hole mergers and the early inspiral of heavy LIGO-Virgo-KAGRA sources. Future time reference, oscillator, and clock technologies realistically expected in the next decade(s) would enable the detection of an increasingly diverse set of sources and allow APTA to reach a better sensitivity than other detector concepts proposed for the decihertz band. This work opens up a new area of research into designing and constructing gravitational-wave detectors relying on principles used successfully in pulsar timing.  

---

## 11. Tidal Resonance in Binary Neutron Star Inspirals: A High-Precision Study in Numerical Relativity

**arXiv**: [2411.16850](https://arxiv.org/abs/2411.16850)  
**Authors**: Hao-Jui Kuan, Kenta Kiuchi, Masaru Shibata  
**Date**: 18 Sep 2025  
**Categories**: hep-ph, astro-ph.HE, gr-qc  
**Type**: replaced  

**Abstract**: Tidal Resonance in Binary Neutron Star Inspirals: A High-Precision Study in Numerical Relativity Hao-Jui Kuan, Kenta Kiuchi, Masaru Shibata 5 pages, 4 figures + supplemental material. To appear in Physical Review Letters High Energy Physics - Phenomenology (hep-ph); High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) We investigate the tidal resonance of the fundamental ($f$-)mode in spinning neutron stars, robustly tracing the onset of the excitation to its saturation, using numerical relativity for the first time. We performed long-term ($\approx15$~orbits) fully relativistic simulations of a merger of two highly and retrogradely spinning neutron stars. The resonance window of the $f$-mode is extended by self-interaction, and the nonlinear resonance continues up to the final plunging phase. We observe that the quasi-circular orbit is maintained throughout since the dissipation of orbit motion due to the resonance is coherent with that due to gravitational waves. The $f$-mode resonance causes a variation in the stellar spin of $\gtrsim6.3\%$ in the linear regime and much more as $\sim33\%$ during the later nonlinear regime. At the merger, a phase shift of $\lesssim40$~radians is rendered in the gravitational waveform as a consequence of the angular momentum and energy transfers into the neutron star oscillations.  

---

## 12. Is your stochastic signal really detectable?

**arXiv**: [2412.10468](https://arxiv.org/abs/2412.10468)  
**Authors**: Federico Pozzoli, Jonathan Gair, Riccardo Buscicchio, Lorenzo Speri  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.IM, astro-ph.HE, gr-qc  
**Type**: replaced  

**Abstract**: Is your stochastic signal really detectable? Federico Pozzoli, Jonathan Gair, Riccardo Buscicchio, Lorenzo Speri Phys.Rev.D 112,064035 - Published 15 September, 2025 Instrumentation and Methods for Astrophysics (astro-ph.IM); High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) Separating a stochastic gravitational wave background (SGWB) from noise is a challenging statistical task. One approach to establishing a detection criterion for the SGWB is using Bayesian evidence. If the evidence ratio (Bayes factor) between models with and without the signal exceeds a certain threshold, the signal is considered detected. We present a formalism to compute the averaged Bayes factor, incorporating instrumental-noise and SGWB uncertainties. As an example, we consider the case of power-law-shaped SGWB in LISA and generate the corresponding Bayesian sensitivity curve. Unlike existing methods in the literature, which typically neglect uncertainties in both the signal and noise, our approach provides a reliable and realistic alternative. This flexible framework opens avenues for more robust stochastic gravitational wave background detection across gravitational-wave experiments.  

---

## 13. Wave-particle duality in the measurement of gravitational radiation

**arXiv**: [2504.03527](https://arxiv.org/abs/2504.03527)  
**Authors**: Hudson A. Loughlin, Germain Tobar, Evan D. Hall, Vivishek Sudhir  
**Date**: 18 Sep 2025  
**Categories**: quant-ph, gr-qc  
**Type**: replaced  

**Abstract**: Wave-particle duality in the measurement of gravitational radiation Hudson A. Loughlin, Germain Tobar, Evan D. Hall, Vivishek Sudhir Quantum Physics (quant-ph); General Relativity and Quantum Cosmology (gr-qc); Optics (physics.optics) In a consistent description of the quantum measurement process, whether the wave or particle-like aspect of a system is revealed depends on the details of the measurement chain, and cannot be interpreted as an objective fact about the system independent of the measurement. We show precisely how this comes to be in the measurement of gravitational radiation. Whether a wave or particle-like aspect is revealed is a property of the detector employed at the end of the quantum measurement chain, rather than of the meter, such as a gravitational-wave (GW) antenna or resonant bar, used to couple the radiation to the detector. A linear detector yields no signal for radiation in a Fock state and a signal proportional to the amplitude in a coherent state -- supporting a wave-like interpretation. By contrast, the signal from a detector coupled to the meter's energy is non-zero only when the incident radiation contains at least a single graviton. Thus, conceptually simple modifications of contemporary GW antennae can reveal wave-particle duality in the measurement of gravitational radiation.  

---

## 14. Letter of Intent: AICE - 100m Atom Interferometer Experiment at CERN

**arXiv**: [2509.11867](https://arxiv.org/abs/2509.11867)  
**Authors**: Charles Baynham, Andrea Bertoldi, Diego Blas, Oliver Buchmueller, Sergio Calatroni, Vassilis Charmandaris, Maria Luisa Chiofalo, Pierre Cladé, Jonathon Coleman, Fabio Di Pumpo, John Ellis, Naceur Gaaloul, Saïda Guellati-Khelifa, Tiffany Harte, Richard Hobson, Michael Holynski, Samuel Lellouch, Lucas Lombriser, Elias Lopez Asamar, Michele Maggiore, Christopher McCabe, Jeremiah Mitchell, Ernst M. Rasel, Federico Sanchez Nieto, Wolfgang Schleich, Dennis Schlippert, Ulrich Schneider, Steven Schramm, Marcelle Soares-Santos, Guglielmo M. Tino, Jonathan N. Tinsley, Tristan Valenzuela, Maurits van der Grinten, Wolf von Klitzing  
**Date**: 18 Sep 2025  
**Categories**: hep-ex, astro-ph.IM, gr-qc, quant-ph  
**Type**: replaced  

**Abstract**: Letter of Intent: AICE - 100m Atom Interferometer Experiment at CERN Charles Baynham, Andrea Bertoldi, Diego Blas, Oliver Buchmueller, Sergio Calatroni, Vassilis Charmandaris, Maria Luisa Chiofalo, Pierre Cladé, Jonathon Coleman, Fabio Di Pumpo, John Ellis, Naceur Gaaloul, Saïda Guellati-Khelifa, Tiffany Harte, Richard Hobson, Michael Holynski, Samuel Lellouch, Lucas Lombriser, Elias Lopez Asamar, Michele Maggiore, Christopher McCabe, Jeremiah Mitchell, Ernst M. Rasel, Federico Sanchez Nieto, Wolfgang Schleich, Dennis Schlippert, Ulrich Schneider, Steven Schramm, Marcelle Soares-Santos, Guglielmo M. Tino, Jonathan N. Tinsley, Tristan Valenzuela, Maurits van der Grinten, Wolf von Klitzing 16 pages, including figures and appendices. Submitted to CERN LHCC as Letter of Intent. arXiv admin note: substantial text overlap with arXiv:2304.00614 High Energy Physics - Experiment (hep-ex); Instrumentation and Methods for Astrophysics (astro-ph.IM); General Relativity and Quantum Cosmology (gr-qc); Atomic Physics (physics.atom-ph); Quantum Physics (quant-ph) We propose an O(100)m Atom Interferometer (AI) experiment - AICE - to be installed against a wall of the PX46 access shaft to the LHC. This experiment would probe unexplored ranges of the possible couplings of bosonic ultralight dark matter (ULDM) to atomic constituents and undertake a pioneering search for gravitational waves (GWs) at frequencies intermediate between those to which existing and planned experiments are sensitive, among other fundamental physics studies. A conceptual feasibility study showed that this AI experiment could be isolated from the LHC by installing a shielding wall in the TX46 gallery, and surveyed issues related to the proximity of the LHC machine, finding no technical obstacles. A detailed technical implementation study has shown that the preparatory civil-engineering work, installation of bespoke radiation shielding, deployment of access-control systems and safety alarms, and installation of an elevator platform could be carried out during LS3, allowing installation and operation of the AICE detector to proceed during Run 4 without impacting HL-LHC operation. These studies have established that PX46 is a uniquely promising location for an AI experiment. We foresee that, if the CERN management encourages this Letter of Intent, a significant fraction of the Terrestrial Very Long Baseline Atom Interferometer (TVLBAI) Proto-Collaboration may wish to contribute to AICE.  

---

## 15. Probing Flavour Deconstruction via Primordial Gravitational Waves

**arXiv**: [2509.12414](https://arxiv.org/abs/2509.12414)  
**Authors**: Noemi Fabri, Gino Isidori, Davide Racco  
**Date**: 18 Sep 2025  
**Categories**: hep-ph, astro-ph.CO  
**Type**: cross-list from hep-ph  

**Abstract**: Probing Flavour Deconstruction via Primordial Gravitational Waves Noemi Fabri, Gino Isidori, Davide Racco High Energy Physics - Phenomenology (hep-ph); Cosmology and Nongalactic Astrophysics (astro-ph.CO) We study the production of primordial gravitational waves (GWs) from first-order phase transitions (FOPTs) in extensions of the Standard Model based on Flavour Deconstruction (FD). The link fields inherent to FD generically form a rich scalar sector, with sizeable couplings at the TeV scale, providing natural conditions for strong FOPTs and correspondingly large GW emission. We identify the key parameters controlling the GW spectrum and enabling its detection at future GW observatories. In particular, we find that while FD scenarios can yield detectable signals, the resulting spectra typically peak at higher frequencies than the millihertz range. As a consequence, a positive observation at LISA is possible but not guaranteed, while the signal falls in the range of mid-band proposals, making FD models an intriguing target for upcoming GW searches.  

---

## 16. Cogenesis of baryon and lepton number asymmetries matching the EMPRESS Data

**arXiv**: [2509.13098](https://arxiv.org/abs/2509.13098)  
**Authors**: Kyu Jung Bae, Arghyajit Datta, Rinku Maji, Wan-Il Park  
**Date**: 18 Sep 2025  
**Categories**: hep-ph, astro-ph.CO  
**Type**: cross-list from hep-ph  

**Abstract**: Cogenesis of baryon and lepton number asymmetries matching the EMPRESS Data Kyu Jung Bae, Arghyajit Datta, Rinku Maji, Wan-Il Park High Energy Physics - Phenomenology (hep-ph); Cosmology and Nongalactic Astrophysics (astro-ph.CO) We show that a simple supersymmetric $U(1)_{B-L}$ extension of the standard model can explain simultaneously the large electron neutrino asymmetry hinted by the recent EMPRESS data as well as the observed tiny baryon number asymmetry via the resonant leptogenesis mechanism. The condensation of $B-L$ Higgs dominating the universe at its decay is the sole source for these generation processes. Here, the infrequent decays of the $B-L$ Higgs to heavy right handed neutrinos and successive prompt decays of these right handed neutrinos around the electroweak phase transition produce the observed baryon number asymmetry, while the complete decay of the same $B-L$ Higgs at a later epoch leads to a large lepton number asymmetry. The right amounts of both asymmetries are found to be obtained for the symmetry-breaking scale $v_\phi \sim 10^{10}~{\rm GeV}$. Moreover, in a close connection to the positivity of both asymmetries, seemingly only the normal mass hierarchy of light neutrino species works. Finally, the gravitational wave background from the topologically stable strong type-I cosmic strings, generated from the breaking of $U(1)_{B-L}$ symmetry, can be within the reach of future experiments such as ultimate DECIGO.  

---

## 17. Revisiting axion dark matter with nonlinear transitions

**arXiv**: [2509.13292](https://arxiv.org/abs/2509.13292)  
**Authors**: Max Miyazaki, Yuma Narita, Deheng Song, Nemin Yaginuma, Wen Yin  
**Date**: 18 Sep 2025  
**Categories**: hep-ph, astro-ph.CO  
**Type**: cross-list from hep-ph  

**Abstract**: Revisiting axion dark matter with nonlinear transitions Max Miyazaki, Yuma Narita, Deheng Song, Nemin Yaginuma, Wen Yin High Energy Physics - Phenomenology (hep-ph); Cosmology and Nongalactic Astrophysics (astro-ph.CO) Recently, two of the present authors showed that even when the axion momentum is much smaller than its mass, the axion can still behave like radiation if its energy density greatly exceeds the maximum potential energy set by the cosine-type potential. As the energy density redshifts down to the potential scale, a nonlinear transition occurs, during which the axion's adiabatic invariant is not conserved. In this paper, we revisit the analysis of axion dark matter by incorporating the effects of this nonlinear transition through a precise study of the axion spectrum. We demonstrate that in the parameter region with a relatively small decay constant, often favored in axion search experiments, special care is required when estimating the axion abundance and spectrum. We also highlight a scenario in which axions are produced through the stimulated decay of a modulus, a situation that may naturally arise in the string axiverse, where the nonlinear transition occurs across a wide parameter region. Furthermore, we discuss related phenomena, including QCD axion dark matter, the formation of axion clumps such as miniclusters and axion stars, gravitational wave production, and formation of primordial black holes as dark matter.  

---

## 18. Star-Black Hole Interactions in Young Star Clusters

**arXiv**: [2509.12318](https://arxiv.org/abs/2509.12318)  
**Authors**: Sara Rastello, Giuliano Iorio, Mark Gieles, Long Wang  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.HE, astro-ph.GA, astro-ph.SR  
**Type**: new submission  

**Abstract**: Star-Black Hole Interactions in Young Star Clusters Sara Rastello, Giuliano Iorio, Mark Gieles, Long Wang Proceedings contribution to IAU Symposium 398 (MODEST-25); to appear in the IAU Proceedings Series. 4 pages, 3 figures High Energy Astrophysical Phenomena (astro-ph.HE); Astrophysics of Galaxies (astro-ph.GA); Solar and Stellar Astrophysics (astro-ph.SR) Close encounters between stars and black holes can trigger micro-tidal disruption events (micro-TDEs) in dense young star clusters (YSCs). Using direct N-body simulations with PETAR, we found that most micro-TDEs arise from few-body multiple encounters. The inferred rate is approximately 350-450 Gpc$^{-3}$ yr$^{-1}$. Micro-TDEs could be detected both by upcoming surveys such as LSST, expected to observe roughly 10-100 events per year, and by their gravitational-wave (GW) signals peaking in the deci-Hertz band, detectable with future instruments such as LGWA and DECIGO.  

---

## 19. The Photospheric Emission of a Short-Duration Gamma-Ray Burst Emerging from a Realistic Binary Neutron Star Merger

**arXiv**: [2509.12505](https://arxiv.org/abs/2509.12505)  
**Authors**: Nathan Walker, Davide Lazzati, Tyler Parsotan, Rosalba Perna  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: The Photospheric Emission of a Short-Duration Gamma-Ray Burst Emerging from a Realistic Binary Neutron Star Merger Nathan Walker, Davide Lazzati, Tyler Parsotan, Rosalba Perna High Energy Astrophysical Phenomena (astro-ph.HE) The almost simultaneous detection of GRB170817A and GW170817 ushered in nearly a decade of interest in binary neutron star mergers and their multi-messenger signals, resulting in a greater understanding of the processes that produce short-duration gamma-ray bursts and gravitational waves. However, open questions remain regarding the emission mechanism of these bursts. In this work we present results from the first study of an electromagnetic signal produced from a realistic treatment of a binary neutron star merger, both for on-axis and off-axis observations. We accomplish this by using the PLUTO hydrodynamical code to inject a relativistic jet into the ejecta of a realistic binary neutron star merger, which was itself obtained from the simulation of a 3D BNS merger. Then, we model the prompt photospheric emission that would emerge from this jet using the MCRaT radiative transfer code. We find that the resulting photon spectra can peak around ~1 MeV for on-axis emission and falls off noticeably for off-axis observations. We also find distinctly non-thermal low and high-energy tails in multiple observations, ranging from shallow to mid-off axis observations. Our on-axis results are consistent with the Amati Correlation for short bursts, with some strain evident at higher observing angles. Finally, we find that the radiative efficiency is much lower than seen in previous studies of the photospheric emission of long-duration gamma-ray bursts.  

---

## 20. Deciphering Profile Stability in Millisecond Pulsars: Timescales, Frequency Evolution, and Implications on Emission Mechanisms

**arXiv**: [2509.12781](https://arxiv.org/abs/2509.12781)  
**Authors**: Ankita Ghosh, Bhaswati Bhattacharyya, Rahul Sharan, Patrick Weltevrede, Jayanta Roy, Sangita Kumari  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: Deciphering Profile Stability in Millisecond Pulsars: Timescales, Frequency Evolution, and Implications on Emission Mechanisms Ankita Ghosh, Bhaswati Bhattacharyya, Rahul Sharan, Patrick Weltevrede, Jayanta Roy, Sangita Kumari Accepted for publication in the Astrophysical Journal High Energy Astrophysical Phenomena (astro-ph.HE) Pulse profile stability in millisecond pulsars (MSPs) is a key factor in achieving high-precision timing essential for detecting nanohertz gravitational waves with Pulsar Timing Arrays (PTAs). In this work, we present a systematic analysis of profile stabilization timescales in MSPs using a direct method based on pulse stacking, applied to long-term multi-epoch observations. Our study utilizes data from the upgraded GMRT (uGMRT) between 300--750 MHz for nine MSPs over 3--5 years and Parkes Ultra-Wideband low-frequency receiver observations (Parkes UWL; covering 704--4032 MHz) for three of them. We find that stable profiles typically require averaging over $10^{5}$--$10^{6}$ pulses. This is the first time such a quantitative approach has been applied to MSPs across a wide frequency range, providing an indirect but practical estimate of jitter noise, a dominant noise source in PTA datasets. We observe that stabilization timescales depend on signal-to-noise ratio, pulse morphology, and surface magnetic field strength, with a moderate correlation indicating a possible role of the magnetic field in emission stability. A complementary single-epoch analysis of nine bright MSPs with uGMRT Band-3 (300--500 MHz) reinforces these results and demonstrates the method's applicability to broader MSP populations. We show that a strong correlation exists between profile-stability slope and the jitter parameter, implying that for faint MSPs, profile-stability analysis can act as an effective proxy for intrinsic pulse-shape variability. Our work provides a novel and scalable framework to assess intrinsic profile variability, helping to guide integration time choices and reduce timing noise in PTA experiments.  

---

## 21. Archival Search for IceCube Sub-TeV Neutrino Counterparts to Sub-Threshold Gravitational Wave Events from the Third Observing Run of the LIGO-Virgo-KAGRA

**arXiv**: [2509.13003](https://arxiv.org/abs/2509.13003)  
**Authors**: Tista Mukherjee  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: Archival Search for IceCube Sub-TeV Neutrino Counterparts to Sub-Threshold Gravitational Wave Events from the Third Observing Run of the LIGO-Virgo-KAGRA Tista Mukherjee (for the IceCube Collaboration) Presented at the 39th International Cosmic Ray Conference (ICRC2025) High Energy Astrophysical Phenomena (astro-ph.HE) The IceCube Neutrino Observatory actively participates in multimessenger follow-ups of gravitational-wave (GW) events. With the release of the Gravitational-Wave Transient Catalogue (GWTC)-2.1 and -3, the sub-threshold GW event information from the third observation run of the LIGO-Virgo-KAGRA (LVK) detectors is publicly available. These sub-threshold GWs are identified via template-based and minimally modelled search pipelines. Neutrino counterparts can enhance their astrophysical significance and improve their localisation. In this contribution, we propose a catalogue-based search for sub-TeV neutrino counterparts to sub-threshold GWs. For this search, we use archival data from IceCube's dense infill array, DeepCore. Using the unbinned maximum likelihood method, we search for correlation between IceCube sub-TeV neutrinos and the $\sim$ 100 most significant sub-threshold GW source candidates. With this study, we aim to contribute to the ongoing efforts to identify common astrophysical sources of neutrinos and GWs. We present the current status of this search and its role in advancing multimessenger astronomy, paving the way for deeper exploration of GW events and their sources.  

---

## 22. Hyperons in Neutron Stars across the observed mass range: Insights from realistic $Λ$-N and $Λ$-$Λ$ interactions within a Microscopic Framework

**arXiv**: [2509.12881](https://arxiv.org/abs/2509.12881)  
**Authors**: Ali Mohammad Ali Looee, Mahboubeh Shahrbaf, Hamid Reza Moshfegh  
**Date**: 18 Sep 2025  
**Categories**: nucl-th, astro-ph.HE  
**Type**: cross-list from nucl-th  

**Abstract**: Hyperons in Neutron Stars across the observed mass range: Insights from realistic $Λ$-N and $Λ$-$Λ$ interactions within a Microscopic Framework Ali Mohammad Ali Looee, Mahboubeh Shahrbaf, Hamid Reza Moshfegh Nuclear Theory (nucl-th); High Energy Astrophysical Phenomena (astro-ph.HE) We investigate the equation of state (EOS) and macroscopic properties of neutron stars (NSs) and hyperonic stars within the framework of the lowest order constrained variational (LOCV) method, extended to include interacting $\Lambda$ hyperons. The nucleon-nucleon interaction is modeled using the AV18 potential supplemented by Urbana three-body forces, while $\Lambda N$ and $\Lambda \Lambda$ interactions are described by realistic spin- and parity-dependent potentials fitted to hypernuclear data. Cold, charge-neutral, and $\beta$-equilibrated matter composed of neutrons, protons, electrons, muons, and $\Lambda$ hyperons is considered. We compute particle fractions, chemical potentials, the EOS, speed of sound, tidal deformability, and stellar structure by solving the Tolman-Oppenheimer-Volkoff equations, and compare our results with recent NICER and gravitational-wave observations. The inclusion of $\Lambda$ hyperons leads to EOS softening, reducing the maximum NS mass from $2.34M_\odot$ to $2.07M_\odot$, while keeping it consistent with the $2M_\odot$ mass constraint. At $1.4M_\odot$, the model satisfies observational limits on radius and tidal deformability, with the $\Lambda$ onset occurring below this mass. Comparison with other microscopic and relativistic mean-field models shows that our EOS remains consistent with the allowed pressure-energy density range, while also permitting even canonical-mass NSs of about $1.4M_{\odot}$ to accommodate hyperons. These results suggest that hyperons can appear in NSs across the observed mass range without violating current astrophysical constraints, and that the extended LOCV method provides a consistent, microscopic approach to modeling dense hypernuclear matter.  

---

## 23. Constraints on the early growth of massive black holes from PTA and JWST with L-GalaxiesBH

**arXiv**: [2509.12325](https://arxiv.org/abs/2509.12325)  
**Authors**: Silvia Bonoli, David Izquierdo-Villalba, Daniele Spinoso, Monica Colpi, Alberto Sesana, Markos Polkas, Volker Springel  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.GA  
**Type**: new submission  

**Abstract**: Constraints on the early growth of massive black holes from PTA and JWST with L-GalaxiesBH Silvia Bonoli, David Izquierdo-Villalba, Daniele Spinoso, Monica Colpi, Alberto Sesana, Markos Polkas, Volker Springel Submitted to A&A. Comments are welcome Astrophysics of Galaxies (astro-ph.GA) Recent Pulsar Timing Arrays (PTAs) results provided strong evidence for a stochastic gravitational wave background (sGWB), consistent with a population of merging massive black holes (MBHs) at $z<1$. Meanwhile, JWST observations at $z>5$ suggest a higher number density of accreting MBHs than previously estimated. Together with constraints from local MBHs and high-$z$ quasars, these findings offer a unique opportunity to test MBH seeding and early growth models. We explore this using ${\tt L-Galaxies}\textit{BH}$, a new extension of the galaxy formation model ${\tt L-Galaxies}$, developed to explicitly model all stages of MBH evolution, including seeding, accretion, and binary dynamics. To take advantage of both the high resolution of the ${\tt MillenniumII}$ and the large volume of the ${\tt Millennium}$ simulations, we run ${\tt L-Galaxies}\textit{BH}$ on the former and use its outputs as initial conditions for the latter, via our $\textit{grafting}$ method. We find that reproducing the number density of high-$z$ active MBHs observed by JWST requires either a heavy seed formation rate significantly higher than that predicted by current models ($\gtrsim 0.01 Mpc^{-3}$ at $z \sim 10$), or widespread formation of light seeds undergoing multiple phases of super-Eddington accretion. Furthermore, matching the amplitude of the PTA sGWB signal requires nearly all galaxies with stellar masses $M_{*}> 10^9 M_\odot$ to host central MBHs by $z\sim0$. Given the extreme heavy seed densities required to satisfy both PTA and JWST constraints, our results favor a scenario in which MBHs originate from light seeds that grow rapidly and efficiently in the early universe. This work demonstrates the power of combining multi-messenger data with physical models to probe the origins and evolution of MBHs across cosmic time.  

---

## 24. The nature and evolution of a-C(:H) nanoparticle substructures and speculations on the origin of the 3-4$μ$m emission bands

**arXiv**: [2509.13119](https://arxiv.org/abs/2509.13119)  
**Authors**: Ant Jones  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.GA  
**Type**: new submission  

**Abstract**: The nature and evolution of a-C(:H) nanoparticle substructures and speculations on the origin of the 3-4$μ$m emission bands Ant Jones 9 pages, 2 tables and 5 figures. Accepted for publication in A&A 14 September 2025 Astrophysics of Galaxies (astro-ph.GA) The nature and evolution of hydrocarbonaceous grains within interstellar and circumstellar media is still far from resolved, perhaps owing to the rather complex nature of their seemingly simple binary atomic compositions. This work explores the fine details of amorphous hydrocarbon nanoparticle, a-C(:H), composition and the evolution of the inherent sub-structures under extreme conditions, focusing on the characteristic CH$_n$ bands in the 3-4 micron wavelength region. Particular attention is paid to the role of dehydrogenation and its effects on the sp^3 and sp^2 hybridisations, leading to an extensive conjugated domain functionalisation of the contiguous structural network within a-C(:H) nanoparticles. Qualitatively this approach is able to explain the origin and evolution, including the appearance and disappearance, of emission bands observed in the 3-4 micron wavelength regime without a significant aromatic moiety content within the structures. A diatomic a-C(:H) phase is likely at the heart of the observed dust evolution in the interstellar medium, and circumstellar and photodissociation regions, as observed at short wavelengths. It appears that we have some way to go in fully understanding these complex materials. Much laboratory work will be required in order to elucidate their chemical and structural evolution at nanoparticle sizes under extreme conditions.  

---

## 25. Binary imposters: Mergers in massive hierarchical triple stars

**arXiv**: [2509.13009](https://arxiv.org/abs/2509.13009)  
**Authors**: F. Kummer, G. Simion, S. Toonen, A. de Koter  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.SR  
**Type**: new submission  

**Abstract**: Binary imposters: Mergers in massive hierarchical triple stars F. Kummer, G. Simion, S. Toonen, A. de Koter Solar and Stellar Astrophysics (astro-ph.SR) Massive stars are often born in triples, where gravitational dynamics and stellar interactions play a crucial role in shaping their evolution. One such pathway includes the merger of the inner binary, transforming the system to a binary with a distinct formation history. Therefore, the interpretation of observed binary properties and their inferred formation history may require the consideration of a potential triple origin. We aim to investigate the population of stellar mergers in massive hierarchical triples. Specifically, we assess how frequently mergers occur, and characterise the properties of the post-merger binaries and their subsequent evolution. We combine the triple population synthesis code TRES, which self-consistently models stellar evolution, binary interaction, and gravitational dynamics, with the binary population synthesis code SeBa to simulate 10^5 dynamically stable, massive triples from the zero-age main sequence through merger and post-merger evolution. We explore the effects of a range of physical models for the initial stellar properties, mass transfer, and merger. We find that stellar mergers are a common outcome, occurring in 20-32% of massive triples. Most mergers happen relatively early in the evolution of the system and involve two main-sequence (MS) stars, producing rejuvenated merger remnants that can appear significantly younger than their tertiary companions. Consequently, we predict that 2-10% of all wide MS+MS binaries (P>100 days) have a measurable age discrepancy, and serve as a promising way to identify merged stars. The post-merger systems preferentially evolve into wide, eccentric binaries, with ~80% avoiding further interaction. However, a notable fraction (16-22%) undergoes a second mass-transfer phase, which may result in the formation of high-mass X-ray binaries or mergers of compact objects that spiral in via gravitational-wave emission.  

---

## 26. Catastrophic disruption of asteroid 2023 CX1 and implications for planetary defense

**arXiv**: [2509.12362](https://arxiv.org/abs/2509.12362)  
**Authors**: Auriane Egal, Denis Vida, François Colas, Brigitte Zanda, Sylvain Bouley, Asma Steinhausser, Pierre Vernazza, Ludovic Ferrière, Jérôme Gattacceca, Mirel Birlan, Jérémie Vaubaillon, Karl Antier, Simon Anghel, Josselin Desmars, Kévin Baillié, Lucie Maquet, Sébastien Bouquillon, Adrien Malgoyre, Simon Jeanne, Jiři Borovička, Pavel Spurný, Hadrien A. R. Devillepoix, Marco Micheli, Davide Farnocchia, Shantanu Naidu, Peter Brown, Paul Wiegert, Krisztián Sárneczky, András Pál, Nick Moskovitz, Theodore Kareta, Toni Santana-Ros, Alexis Le Pichon, Gilles Mazet-Roux, Julien Vergoz, Luke McFadden, Jelle Assink, Läslo Evers, Daniela Krietsch, Henner Busemann, Colin Maden, Lisa Maria Eckart, Jean-Alix Barrat, Pavel Povinec, Ivan Sykora, Ivan Kontul', Oscar Marchhart, Martin Martschini, Silke Merchel, Alexander Wieser, Matthieu Gounelle, Sylvain Pont, Pierre Sans-Jofre, Sebastiaan de Vet, Ioannis Baziotis, Miroslav Brož, Michaël Marsset, Jérôme Vergne, Josef Hanuš, Maxime Devogèle, Luca Conversi, Francisco Ocaña, Luca Buzzi, Dan Alin Nedelcu, Adrian Sonka, Florent Losse, Philippe Dupouy, Korado Korlević, Dieter Husar, Jost Jahn, Damir Šegon, Mark McIntyre, Ralf Neubert, Pierre Beck, Patrick Shober, Anthony Lagain, Josep Maria Trigo-Rodriguez, Enrique Herrero, Jim Rowe, Andrew R.D. Smedley, Ashley King, Salma Sylla, Daniele Gardiol, Dario Barghini, Hervé Lamy, Emmanuel Jehin, Detlef Koschny, Bjorn Poppe, Andrés Jordán, Rene A. Mendez, Katherine Vieira, Hebe Cremades, Hasnaa Chennaoui Aoudjehane, Zouhair Benkhaldoun, Olivier Hernandez, Darrel Robertson, Peter Jenniskens  
**Date**: 18 Sep 2025  
**Categories**: astro-ph.EP, astro-ph.IM  
**Type**: cross-list from astro-ph.EP  

**Abstract**: Catastrophic disruption of asteroid 2023 CX1 and implications for planetary defense Auriane Egal, Denis Vida, François Colas, Brigitte Zanda, Sylvain Bouley, Asma Steinhausser, Pierre Vernazza, Ludovic Ferrière, Jérôme Gattacceca, Mirel Birlan, Jérémie Vaubaillon, Karl Antier, Simon Anghel, Josselin Desmars, Kévin Baillié, Lucie Maquet, Sébastien Bouquillon, Adrien Malgoyre, Simon Jeanne, Jiři Borovička, Pavel Spurný, Hadrien A. R. Devillepoix, Marco Micheli, Davide Farnocchia, Shantanu Naidu, Peter Brown, Paul Wiegert, Krisztián Sárneczky, András Pál, Nick Moskovitz, Theodore Kareta, Toni Santana-Ros, Alexis Le Pichon, Gilles Mazet-Roux, Julien Vergoz, Luke McFadden, Jelle Assink, Läslo Evers, Daniela Krietsch, Henner Busemann, Colin Maden, Lisa Maria Eckart, Jean-Alix Barrat, Pavel Povinec, Ivan Sykora, Ivan Kontul', Oscar Marchhart, Martin Martschini, Silke Merchel, Alexander Wieser, Matthieu Gounelle, Sylvain Pont, Pierre Sans-Jofre, Sebastiaan de Vet, Ioannis Baziotis, Miroslav Brož, Michaël Marsset, Jérôme Vergne, Josef Hanuš, Maxime Devogèle, Luca Conversi, Francisco Ocaña, Luca Buzzi, Dan Alin Nedelcu, Adrian Sonka, Florent Losse, Philippe Dupouy, Korado Korlević, Dieter Husar, Jost Jahn, Damir Šegon, Mark McIntyre, Ralf Neubert, Pierre Beck, Patrick Shober, Anthony Lagain, Josep Maria Trigo-Rodriguez, Enrique Herrero, Jim Rowe, Andrew R.D. Smedley, Ashley King, Salma Sylla, Daniele Gardiol, Dario Barghini, Hervé Lamy, Emmanuel Jehin, Detlef Koschny, Bjorn Poppe, Andrés Jordán, Rene A. Mendez, Katherine Vieira, Hebe Cremades, Hasnaa Chennaoui Aoudjehane, Zouhair Benkhaldoun, Olivier Hernandez, Darrel Robertson, Peter Jenniskens This preprint has not undergone peer review (when applicable) or any post-submission improvements or corrections. The Version of Record of this article is published in \textit{Nature Astronomy}, and is available online at this https URL Earth and Planetary Astrophysics (astro-ph.EP); Instrumentation and Methods for Astrophysics (astro-ph.IM) Mitigation of the threat from airbursting asteroids requires an understanding of the potential risk they pose for the ground. How asteroids release their kinetic energy in the atmosphere is not well understood due to the rarity of significant impacts. Ordinary chondrites, in particular L chondrites, represent a frequent type of Earth-impacting asteroids. Here, we present the first comprehensive, space-to-lab characterization of an L chondrite impact. Small asteroid 2023 CX1 was detected in space and predicted to impact over Normandy, France, on 13 February 2023. Observations from multiple independent sensors and reduction techniques revealed an unusual but potentially high-risk fragmentation behavior. The nearly spherical 650 $\pm$ 160 kg (72 $\pm$ 6 cm diameter) asteroid catastrophically fragmented around 28 km altitude, releasing 98% of its total energy in a concentrated region of the atmosphere. The resulting shockwave was spherical, not cylindrical, and released more energy closer to the ground. This type of fragmentation increases the risk of significant damage at ground level. These results warrant consideration for a planetary defense strategy for cases where a >3-4 MPa dynamic pressure is expected, including planning for evacuation of areas beneath anticipated disruption locations.  

---

