# Direct Preference Optimization

当前主要通过RLHF来将模型和人类偏好对齐，但是RLHF本身是一个非常复杂并且不稳定的过程。本文介绍了RLHF中奖励模型的一种新的参数化方法DPO，该方法能够以封闭形式提取相应的最优策略，使我们能够仅通过简单的分类损失来解决标准RLHF问题。

DPO的特点是稳定（stable）、高性能（preformant）、计算量轻（computationally lightweight），在微调或调整超参时不需要基于LM采样。

DPO（Direct Preference Optimization）
