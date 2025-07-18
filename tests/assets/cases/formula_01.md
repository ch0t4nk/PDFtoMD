(3) Maj1@N (majority-voting-at-N): $N$ sampled solutions are first clustered by their math equivalence, i.e., $g(A_i, A_j)$. Then, one solution $A^*$ from a most frequent cluster is selected for calculating the accuracy, $g(A, A^*)$.

(4) MajK@N: Similar to Pass@N, we define an oracle that always selects the correct solution when it is presented in the top-K majority-voting clusters, $\{A_1^*, A_2^*,..., A_K^*\}$, so its accuracy is $\max_{k\in\{1,2,...,K\}} g(A, A_k^*)$.

Another line of work leverages external tools such as Python programs to enhance the LLMs' ability (Chen et al., 2022; Wu et al., 2023; Yue et al., 2023; Zhou et al., 2023). In this work, we focus on improving the LLMs' inherent ability to solve math problems without help from external tools.

# 3 METHODS

## 1 SUPERVISED SOLUTION FINE-TUNING

In Hendrycks et al. (2021b); Cobbe et al. (2021) models are fine-tuned to generate not only the final answer but also the step-by-step process for solving the math problem.

$S, A \leftarrow M(P)$, (2)

where $P$ is the math problem, $S, A$ are the ground-truth step-by-step solution and the final answer respectively, and $M$ is an LLM. In training, the solution $S$ and the final answer $A$ are concatenated into a single text sequence $X$, and the model is fine-tuned with the cross-entropy loss following the maximum likelihood estimation (MLE) paradigm:

$L_{mle} = -\log p_M(X|P)$, (3)

where $p_M$ is the probably distribution given by the auto-regressive language model $M$:

$p_M(X|P) = \prod_i p_M(x_i|X_{0,...,i-1}, P)$. (4)

Here, $x_i$ is the $i$-th token in $X$, $X_{0,...,i-1}$ is the prefix before $x_i$.

To collect the ground-truth step-by-step solutions, we use two sources: (1) the original human-written solutions in the MATH dataset, (2) GPT-4 generated solutions provided in Lightman et al. (2023) with the chain-of-thought prompting eliciting step-by-step solutions. Our preliminary analysis found that the original solutions in the MATH dataset are more abstract while the solutions generated by GPT-4 are more fine-grained and detailed.

## 2 SOLUTION-CLUSTER RE-RANKING

We note that there are two significant gaps for LLMs' math problem solving performance in Table 2: (1) the gap between the model's greedy-decoding (Pass@1) and majority-voting (Maj1@N) results; (2) the gap between the model's majority-voting best-at-1 (Maj1@N) and best-at-K performance (MajK@N). To narrow these gaps, we fine-tune the pre-trained LLM as a solution verifier/evaluator, following Cobbe et al. (2021). However, unlike in the previous work where a large number (e.g., 1000) of candidate solutions are all reranked by the evaluator, we combine the strength of majority voting and re-ranking together by only re-ranking the top-K solution clusters. We believe this re-ranking strategy is both more robust and cost-efficient, as will be elaborated in the following section.

To use the evaluator to score each candidate solution, we formulate the scoring task as a classification problem in a text completion format, inspired by related work on using LLMs for text evaluation (Liu et al., 2023; Fu et al., 2023). Concretely, we define a mapping function $T$ converting the math problem $P$ and a candidate solution $\tilde{X}$ into a prompt $T(P, \tilde{X})$: "Here is a math problem: $P$. Here is a candidate solution: $\tilde{X}$. The above candidate solution is ". We then interpret the model-predicted probability of the word "correct" (or "incorrect") being the next token¹ as the probability of the solution being correct (or incorrect):

$p_{cls}("correct"|\tilde{X}, P) = p_M("correct"|T(P, \tilde{X}))$, (5)

¹We note that the tokenizer we used tokenizes the words "correct" and "incorrect" both into a single token.