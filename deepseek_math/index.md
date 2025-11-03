<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/katex.min.css" integrity="sha384-WcoG4HRXMzYzfCgiyfrySxx90XSl2rxY5mnVY5TwtWE6KLrArNKn0T/mOgNL0Mmi" crossorigin="anonymous">

# DeepSeekMath

DeepSeek发布DeepSeekMath-7B，在不借助外部工具和vote机制的情况下，在MATH数据集上达到了Gemini-Ultra和GPT4的水准，而在64个sample上做self-consistency指标会进一步提升。DeepSeek自称其数学推理能力来源于两个关键点：数据清洗和强化学习算法GRPO.

## 什么是GRPO？

回顾PPO通过如下代理目标函数来优化策略（policy）：

$$
J_{PPO}(\theta) = \Bbb{E}_{[q \sim P(Q), o \sim \pi_{\theta_{old}}(O|q)]} \frac{1}{|o|}\sum_{t=1}^{|o|}min [\frac{\pi_\theta(o_t|q, o_{<t})}{\pi_{\theta_{old}}(o_t|q, o_{<t})}A_t, clip(\frac{\pi_\theta(o_t|q, o_{<t})}{\pi_{\theta_{old}}(o_t|q, o_{<t})}, 1-\epsilon, 1+\epsilon)A_t]
$$

其中

- $q, o$分别表示question和output，前者采样自dataset，后者来自$\pi_{\theta_{old}}$;
- $\epsilon$是截断超参；
- $A_t$是优势函数，基于rewards ${r_{\ge t}}$和value function $V_{\psi}$用GAE来计算；

PPO需要value function和policy model一起训练，从而缓解reward model过拟合的问题。

标准的方法是在每个token上增加KL惩罚项：

$$
r_t = r_{\varphi}(q, o_{\le t}) - \beta \log \frac{\pi_\theta(o_t|q, o_{\lt t})}{\pi_{\theta_{ref}}(o_t|q, o_{\lt t})}
$$

其中

- $r_{\varphi}$是reward model;
- $\pi_{ref}$是reference model;

由于PPO中的value function是一个和初始SFT大小差不多的模型，所以会带来很大的内存和计算开销。

在RL训练中，为了减少方差，value function会被作为优势计算的baseline

然而在LLM上下文中，reward model只会给最后一个token分配分数，为此提出GRPO，使用多个采样的output的奖励均值作为baseline

具体说，对于每个问题q，采样一组output，然后通过如下代理目标函数来优化策略：

$$

$$

<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/katex.min.js" integrity="sha384-J+9dG2KMoiR9hqcFao0IBLwxt6zpcyN68IgwzsCSkbreXUjmNVRhPFTssqdSGjwQ" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          // customised options
          // • auto-render specific keys, e.g.:
          delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\\(', right: '\\)', display: false},
              {left: '\\[', right: '\\]', display: true}
          ],
          // • rendering keys, e.g.:
          throwOnError : false
        });
    });
</script>