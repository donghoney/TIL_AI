## Local Optima

장소 : AS510

일시 : 2020년 1월 4일 



### Markov Chain Monte Carlo Sampling(MCMC)

* MCMC : Bayesian Inference에서 Target Probability Distribution을 추정하기 위해 분포에 대한 정보를 얻는 방법론

* MCMC Sampling : MCMC에서 Target Probability Distributiond의 분포를 확률적으로 샘플링하는 방법론

* A simple introduction to Markov Chain Monte–Carlo sampling

  * https://link.springer.com/content/pdf/10.3758/s13423-016-1015-8.pdf

* MCMC sequence of development

  * Metropolis-Hastings algorithm

    * Q는 proposal distribution P*(x)는 고차원 pdf이다. 이 때, Q는 랜덤 워크를 샘플링할 분포로 대칭 분포여야하며, 잘 설정되어야 한다. 

  * No- U Turn Sampler(NUTs)

    * https://arxiv.org/pdf/1111.4246.pdf
    * https://github.com/mfouesneau/NUTS

  * Adaptively Preconditioned Stochastic Gradient Langevin Dynamics algorithm

    * https://arxiv.org/pdf/1906.04324.pdf
    * https://github.com/Anirudhsekar96/Noisy_SGD

    