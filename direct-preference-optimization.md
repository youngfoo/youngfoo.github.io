# Direct Preference Optimization

背景

当前主要通过RLHF来将模型和人类偏好对齐，但是RLHF本身是一个非常复杂并且不稳定的过程。
DPO（Direct Preference Optimization）认为LLM本身就是一个RM模型，通过隐式建模直接进行
