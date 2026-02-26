# Complete Daily GW arXiv Digest - 2026-02-26

**总爬取文章**: 181 篇  
**今天的文章**: 180 篇  
  - gr-qc: 27 篇  
  - astro-ph: 134 篇  
**引力波相关**: 11 篇  
**提交类型**: 🆕 4 New • 🔄 2 Cross-lists • 🔄 5 Replacements  

## 1. Likelihood-Based One-Class Scoring in CWT Latent Space for Confusion-Limited LISA Gravitational-Wave Detection

**arXiv**: [2602.20212](https://arxiv.org/abs/2602.20212)  
**Authors**: Jericho Cain  
**Date**: 26 Feb 2026  
**Categories**: gr-qc, astro-ph.IM  
**Type**: new submission  

**Abstract**: Likelihood-Based One-Class Scoring in CWT Latent Space for Confusion-Limited LISA Gravitational-Wave Detection Jericho Cain General Relativity and Quantum Cosmology (gr-qc); Instrumentation and Methods for Astrophysics (astro-ph.IM) We study one-class scoring for resolvable-source detection in confusion-limited LISA time-series data represented as continuous-wavelet-transform (CWT) scalograms. With data generation and preprocessing held fixed, we benchmark geometry-style scoring against likelihood-style latent-density scoring, while also evaluating morphology-augmented and contrastive variants. Geometry-only and geometry+morphology methods provide modest gains over the reconstruction baseline, and contrastive variants do not show stable improvement. Likelihood scoring on AE latents is consistently stronger: across three seeds, latent-only likelihood reaches ROC-AUC $0.8555\pm 0.0181$ and PR-AUC $0.9219 \pm 0.0118$, versus ROC-AUC $0.7663 \pm 0.0450$ and PR-AUC $0.8667 \pm 0.0255$ for AE+manifold. These results indicate that explicit latent density modeling can outperform local off-manifold distance in this confusion-limited regime. We provide seed-based comparisons, unified ROC/PR visual summaries, and reproducible experimental artifacts to support follow-on work in LISA anomaly detection.  

---

## 2. Gravitational wave radiation from periodic orbits in regular black holes

**arXiv**: [2602.20745](https://arxiv.org/abs/2602.20745)  
**Authors**: Rishav Agrawal, Anjan Kar, Soumya Jana, Sayan Kar  
**Date**: 26 Feb 2026  
**Categories**: gr-qc, astro-ph.HE, hep-th  
**Type**: new submission  

**Abstract**: Gravitational wave radiation from periodic orbits in regular black holes Rishav Agrawal (NUS, Singapore), Anjan Kar (IIT Kharagpur, India), Soumya Jana (Sitananda College, India), Sayan Kar (IIT Kharagpur, India) General Relativity and Quantum Cosmology (gr-qc); High Energy Astrophysical Phenomena (astro-ph.HE); High Energy Physics - Theory (hep-th) Gravitational wave radiation from periodic orbits in some standard regular black hole spacetimes is studied, primarily using known methods (numerical and analytic). We demonstrate specific differences with the singular Schwarzschild geometry by analysing orbit characteristics, gravitational wave strain profiles, and the corresponding power spectrum density, for different values of the regularising parameter `$g$'. Further, we assess our results vis-a-vis the LISA sensitivity curves and show how our results may be useful while developing templates for detecting regular black holes as viable alternatives to the singular ones. The appendices to our article contain details on errors in our estimates and provide for the first time, some exact analytical expressions on gravitational wave radiation from different types of periodic orbits in Schwarzschild spacetime.  

---

## 3. 5PN eccentric waveforms for intermediate-mass-ratio-inspirals (IMRIs) from post-Newtonian and black hole perturbation theory

**arXiv**: [2602.21018](https://arxiv.org/abs/2602.21018)  
**Authors**: M Laxman, Ryuichi Fujita, Chandra Kant Mishra  
**Date**: 26 Feb 2026  
**Categories**: gr-qc, astro-ph.HE  
**Type**: new submission  

**Abstract**: 5PN eccentric waveforms for intermediate-mass-ratio-inspirals (IMRIs) from post-Newtonian and black hole perturbation theory M Laxman, Ryuichi Fujita, Chandra Kant Mishra General Relativity and Quantum Cosmology (gr-qc); High Energy Astrophysical Phenomena (astro-ph.HE) Detection of gravitational waves from compact binaries involving at least one intermediate mass black hole, and component mass ratios in the range $0.1$-$10^{-4}$, are among the primary sources for future space detectors with target strain sensitivities in the deci-Hertz (dHz) band. Tuned to the waveform requirements for analyzing such sources, a hybrid model is obtained by combining waveforms from the post-Newtonian (PN) and black hole perturbation (BHP) theory. Components of the binary are assumed to be nonspinning and on eccentric orbits. This hybrid model is 3PN accurate in terms of results from PN theory and 5PN in results from BHP theory. In terms of eccentricity, corrections through the order $\mathcal{O}(e^{10})$ are included. Further, using number of gravitational wave cycles estimates for a few representative binaries observable in the dHz band, we demonstrate the significance of the mass ratio information from the PN approach, of contributions from the BHP theory at high PN orders, and also of higher order eccentricity corrections. In particular, we find an almost 10-fold increase in number of gravitational wave cycles for a fixed mass ratio of 0.1 and $e_0\sim0.3$ (evaluated at $0.01$Hz) when contributions beyond the leading order in eccentricity are accounted for. We also confirm the requirement to go beyond 5PN order in the circular part of the waveform from BHP theory.  

---

## 4. Neural Bayesian updates to populations with growing gravitational-wave catalogs

**arXiv**: [2602.20277](https://arxiv.org/abs/2602.20277)  
**Authors**: Noah E. Wolfe, Matthew Mould, John Veitch, Salvatore Vitale  
**Date**: 26 Feb 2026  
**Categories**: astro-ph.IM, astro-ph.HE, gr-qc  
**Type**: cross-list from astro-ph.IM  

**Abstract**: Neural Bayesian updates to populations with growing gravitational-wave catalogs Noah E. Wolfe, Matthew Mould, John Veitch, Salvatore Vitale 14+6 pages, 9+2 figures; comments welcome! Instrumentation and Methods for Astrophysics (astro-ph.IM); High Energy Astrophysical Phenomena (astro-ph.HE); General Relativity and Quantum Cosmology (gr-qc) As gravitational-wave catalogs grow, they will become increasingly computationally expensive to analyze in their entirety, especially when inferring astrophysical source populations with high-dimensional, flexible models. Bayesian statistics offers a natural remedy, letting us update our knowledge of physical models as new data arrive, without re-analyzing existing data. However, doing so requires the posterior probability density of model parameters for previous observations, which is typically intractable. Here, we use variational neural posterior estimation to rapidly update the inferred population of binary black holes as data are observed in gravitational-wave detectors. We apply this approach to real and simulated catalogs analyzed with both low- and high-dimensional population models, testing the reliability of three update cadences: with new catalogs of sources, month by month during an observing run, and as each new signal arrives. We investigate the success and failure modes of neural sequential updates, finding that the robustness of updating is sensitive to the information contained in each update and that updating is most effective when performed with larger segments of data. We outline one additional scientific application enabled by Bayesian updating: identification of events that are individually informative about the population. Neural Bayesian updates to astrophysical population models also provide efficient likelihood representations for joint analyses with other data, e.g., standard-siren cosmology, and similar methods can be used to perform Bayesian stochastic background searches.  

---

## 5. Bypassing the Lyth Bound with Entangled Gravitons: Primordial Signatures and Late-Time Noise

**arXiv**: [2602.20734](https://arxiv.org/abs/2602.20734)  
**Authors**: Shingo Akama, Chunshan Lin  
**Date**: 26 Feb 2026  
**Categories**: astro-ph.CO, gr-qc  
**Type**: cross-list from astro-ph.CO  

**Abstract**: Bypassing the Lyth Bound with Entangled Gravitons: Primordial Signatures and Late-Time Noise Shingo Akama, Chunshan Lin Cosmology and Nongalactic Astrophysics (astro-ph.CO); General Relativity and Quantum Cosmology (gr-qc) We demonstrate that quantum entanglement between primordial gravitons in dynamically decoupled gravitational sectors can parametrically enhance the tensor power spectrum during inflation. Unlike standard mechanisms relying on classical dynamics or modified actions, this enhancement originates from the reduced density matrix of the observable sector after tracing over a hidden gravitational reservoir. This framework allows for a sizable tensor-to-scalar ratio r > 0.01 consistent with sub-Planckian inflaton excursions, providing a purely quantum mechanical evasion of the Lyth bound. The resulting mixed state leaves a distinctive "quantum birthmark" in the form of oscillatory features in the power spectrum and a characteristic violation of the single-field consistency relation, manifesting as a scale-dependent enhancement of the squeezed-limit bispectrum. Furthermore, we forecast that this entanglement may manifest as a late-time stochastic noise enhancement in gravitational wave interferometers, offering a novel experimental window into the quantum nature of spacetime.  

---

## 6. Probing cosmic strings via gravitational-wave lensing

**arXiv**: [2510.20442](https://arxiv.org/abs/2510.20442)  
**Authors**: Oleg Bulashenko, Nino Villanueva, Roberto Bada Nerin, José A. Font  
**Date**: 26 Feb 2026  
**Categories**: gr-qc, astro-ph.CO, astro-ph.GA, astro-ph.HE  
**Type**: replaced  

**Abstract**: Probing cosmic strings via gravitational-wave lensing Oleg Bulashenko, Nino Villanueva, Roberto Bada Nerin, José A. Font 21 pages, 10 figs, published version with updated title Phys. Rev. D 113, 044063 (2026) General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO); Astrophysics of Galaxies (astro-ph.GA); High Energy Astrophysical Phenomena (astro-ph.HE) We present a framework for detecting gravitational-wave signals lensed by cosmic strings (CSs), addressing a key gap in current searches. CSs, whose detection would provide a unique probe of high-energy physics and the early Universe, possess distinct topological and geometric features that require a dedicated search strategy. Our approach employs a full-wave transmission factor, expressed analytically via Fresnel integrals, which captures the characteristic diffraction and interference effects of the conical spacetime around a straight CS. We contrast CS lensing with the well-studied point mass lens (PML) model, highlighting their fundamental differences: CS lensing depends on cosmological distances, string tension $\Delta$, and wavelength $\lambda$, and produces two non-amplified images set by the global conical geometry. In contrast, PML lensing is governed by the distance-independent ratio $\sim M_{Lz}/\lambda$, where $M_{Lz}$ represents the redshifted mass of the lens, with image properties derived from the lens equation. For BBH mergers lensed by CSs, we show that the waveforms exhibit a characteristic beating pattern or time-separated exact replicas. We derive a detectability bound on the string tension and, using Bayesian model selection, demonstrate that CS lensing is distinguishable from both unlensed and PML-lensed signals across a wide region of parameter space.  

---

## 7. GraviBERT: Transformer-based inference for gravitational-wave time series

**arXiv**: [2512.21390](https://arxiv.org/abs/2512.21390)  
**Authors**: Martin Benedikt, Ippocratis D. Saltas  
**Date**: 26 Feb 2026  
**Categories**: gr-qc, astro-ph.CO, astro-ph.IM  
**Type**: replaced  

**Abstract**: GraviBERT: Transformer-based inference for gravitational-wave time series Martin Benedikt, Ippocratis D. Saltas v2: Text improved for clarity, 2 new figures, references updated, results unchanged. Link with code added General Relativity and Quantum Cosmology (gr-qc); Cosmology and Nongalactic Astrophysics (astro-ph.CO); Instrumentation and Methods for Astrophysics (astro-ph.IM) We introduce GraviBERT, a novel deep learning framework for gravitational wave inference, built on a multi-scale feature extractor with a transformer encoder and a suitable regression head. A key novelty of GraviBERT is its staged training: a BERT-style self-supervised pretraining phase to learn transferable representations, followed by supervised fine-tuning on labeled data. GraviBERT demonstrates consistent transfer learning across detector configurations and waveform models. On in-domain data, pretraining reduces the MAE by up to $31\%$ and accelerates convergence by $\sim 6.6 \times$, with mean relative precision for point estimates reaching the few-percent level and MAE in effective spin of $\sim 10^{-3}$ at SNR = 10. For domain adaptation to new detector noise profiles, the pretrained model converges up to $15\times$ faster on small target datasets and reduces estimation errors by up to $\sim 47\%$, demonstrating detector-agnostic learning. Cross-waveform approximant transfer achieves up to $44\%$ MAE reductions and up to $15\times$ training speedups, with $R^2$ scores consistently exceeding $0.9$ for mass parameters at SNR = 10 compared to $0.74$ - $0.87$ when training from scratch. GraviBERT works directly with noisy waveforms, and in its current form quantifies predictive uncertainty through MC dropouts. After pretraining, the regression head could be adapted to multiple downstream inference tasks in gravitational-wave astronomy.  

---

## 8. Generalized Unitarity Method for Worldline Field Theory

**arXiv**: [2510.00989](https://arxiv.org/abs/2510.00989)  
**Authors**: Vincent F. He, Julio Parra-Martinez  
**Date**: 26 Feb 2026  
**Categories**: hep-th, gr-qc  
**Type**: replaced  

**Abstract**: Generalized Unitarity Method for Worldline Field Theory Vincent F. He, Julio Parra-Martinez 30 pages + refs, 7 figures. v4: Edited based on referee report High Energy Physics - Theory (hep-th); General Relativity and Quantum Cosmology (gr-qc) We present a generalized unitarity method for theories of point-particle worldlines coupled to gravity, analogous to that of scattering amplitudes in quantum field theory. This method allows the computation of perturbative observables from basic principles such as locality and unitarity, thus avoiding gauge redundancies and the use of Feynman diagrams. We illustrate the method with a variety of examples, including the gravitational waveform for the scattering of two point masses at next-to-leading order (or ${\cal O}(G^{5/2})$), reproducing known results. Our method further streamlines the calculation of the scattering dynamics of compact binary systems and opens the door to further applications and systematical exploration of structure in this class of observables.  

---

## 9. Resolving the QCD Axion Domain Wall Problem with a Light Axion

**arXiv**: [2507.07075](https://arxiv.org/abs/2507.07075)  
**Authors**: Junseok Lee, Kai Murai, Fuminobu Takahashi, Wen Yin  
**Date**: 26 Feb 2026  
**Categories**: hep-ph, astro-ph.CO  
**Type**: replaced  

**Abstract**: Resolving the QCD Axion Domain Wall Problem with a Light Axion Junseok Lee, Kai Murai, Fuminobu Takahashi, Wen Yin 17 pages, 7 figures, v2: Published version in JHEP; a typo corrected High Energy Physics - Phenomenology (hep-ph); Cosmology and Nongalactic Astrophysics (astro-ph.CO) We propose two novel solutions to the domain wall problem of the QCD axion by introducing a massless or light axion that also couples to gluons. The first solution applies when the new axion forms strings after inflation. Due to its mixing with the QCD axion, domain walls of the QCD axion are bounded by these strings and confined into cosmologically safe string bundles. This scenario predicts the existence of such string bundles, which may survive until today and leave observable signatures, such as gravitational waves, cosmic birefringence, and CMB anisotropies. The simultaneous detection of the QCD axion and any of these cosmological signatures would serve as a smoking-gun signal. The second solution assumes a homogeneous initial condition for the new axion. If it is sufficiently light, its potential temporarily induces a bias in the QCD axion potential before the onset of oscillations, rendering the domain walls unstable. In both scenarios, the Peccei-Quinn mechanism remains effective, and the strong CP problem is not reintroduced. We identify the viable parameter regions and discuss the resulting dark matter abundance.  

---

## 10. ASKAP J005512.2-255834: A Luminous, Long-Lived Radio Transient at z = 0.1 -- an Orphan Afterglow or an off-nuclear TDE from an IMBH?

**arXiv**: [2602.20522](https://arxiv.org/abs/2602.20522)  
**Authors**: Ashna Gulati, Tara Murphy, David L. Kaplan, Dougal Dobie, Charlotte Ward, Gemma Anderson, Manisha Caleb, Poonam Chandra, Jeff Cooke, Barnali Das, Adam Deller, Adelle Goodwin, Kelly Gourdji, Giancarlo Ghirlanda, Emil Lenc, Anais Möller, James K. Leung, Stella Koch Ocker, Joshua Pritchard, Claudio Ricci, Elaine M. Sadler, Om Sharan Salafia, Kavya Shaji, Roberto Soria, Mark Suhr, Artem Tuntsov, Ziteng Wang  
**Date**: 26 Feb 2026  
**Categories**: astro-ph.HE  
**Type**: new submission  

**Abstract**: ASKAP J005512.2-255834: A Luminous, Long-Lived Radio Transient at z = 0.1 -- an Orphan Afterglow or an off-nuclear TDE from an IMBH? Ashna Gulati, Tara Murphy, David L. Kaplan, Dougal Dobie, Charlotte Ward, Gemma Anderson, Manisha Caleb, Poonam Chandra, Jeff Cooke, Barnali Das, Adam Deller, Adelle Goodwin, Kelly Gourdji, Giancarlo Ghirlanda, Emil Lenc, Anais Möller, James K. Leung, Stella Koch Ocker, Joshua Pritchard, Claudio Ricci, Elaine M. Sadler, Om Sharan Salafia, Kavya Shaji, Roberto Soria, Mark Suhr, Artem Tuntsov, Ziteng Wang This paper has been accepeted for publication in ApJ High Energy Astrophysical Phenomena (astro-ph.HE) We report the discovery of a slowly evolving, extragalactic radio transient, ASKAP J005512.2--255834 (hereafter ASKAP J0055-2558), identified using the Australian SKA Pathfinder in a search for orphan afterglows associated with archival gravitational wave events. Although discovered in this context, there is no evidence that the transient is associated with any known gravitational wave event. Nonetheless, this source exhibits a 20-fold increase in flux density over $<250$ days, and it remains in a declining, detectable state more than 1000 days after the initial detection. Follow-up observations from 0.3 to 9 GHz reveal an evolving spectrum consistent with synchrotron emission. ASKAP J0055-2558 is spatially coincident with a low-mass, star-forming galaxy at redshift $z = 0.116$ ($d_{\rm L}$= 543 Mpc), placing its peak radio luminosity at $\nu L_\nu \sim 10^{39}\,\rm erg\,s^{-1}$. Analysis of its radio light curve, inferred blastwave velocity, energetics, host galaxy properties and the absence of counterparts at other wavelengths suggest that ASKAP J0055-2558 is most consistent with either the late-time phase of an orphan long gamma-ray burst afterglow or a tidal disruption event involving an intermediate-mass black hole spatially offset from the galaxy nucleus. The radio discovery of either of these phenomena is extremely rare, with only a few or no confirmed examples to date.  

---

## 11. Population synthesis of double white dwarfs: evolutionary effects on system properties

**arXiv**: [2602.00724](https://arxiv.org/abs/2602.00724)  
**Authors**: Sreeta Roy, Surajit Kalita  
**Date**: 26 Feb 2026  
**Categories**: astro-ph.SR, astro-ph.HE  
**Type**: replaced  

**Abstract**: Population synthesis of double white dwarfs: evolutionary effects on system properties Sreeta Roy, Surajit Kalita 10 pages with 4 figures; accepted in Publications of the Astronomical Society of Australia; typos corrected Solar and Stellar Astrophysics (astro-ph.SR); High Energy Astrophysical Phenomena (astro-ph.HE) Double white dwarf (DWD) binaries are natural outcomes of binary stellar evolution and key sources for future space-based gravitational wave (GW) observatories such as Laser Interferometer Space Antenna (LISA). We investigate how different binary interaction channels shape the physical and orbital properties of DWD systems, focusing on component masses, orbital separations, core compositions, and mass transfer rates. Using the binary population synthesis code COMPAS, we evolve $10^7$ binaries with physically motivated initial distributions of binary parameters. Our simulations reproduce the strong bimodality in the final orbital separations, including a pronounced deficit of systems around $100-500 \rm\,R_\odot$, arising from distinct evolutionary pathways: wide DWDs predominantly originate from stable Roche lobe overflow (RLOF), while close DWDs form through unstable RLOF leading to at least one common envelope (CE) phase. Moreover, we show that the core compositions of WDs provide a powerful tracer of evolutionary history: He-core WDs are strongly concentrated in close systems, whereas CO-core WDs span the full separation range and exhibit a small mass gap in wide binaries. We further identify a correlation between the donor mass transfer rate and the final orbital separation, highlighting the impact of non-conservative mass transfer on the resulting orbital configuration of DWD systems. These results underscore the links among evolutionary channels, chemical composition, and mass transfer rates; thereby provide a unique framework for interpreting Gaia DWD samples and forecasting the joint electromagnetic and GW population accessible to LISA.  

---

