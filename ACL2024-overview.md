<!doctype html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>youngfoo</title>
    <link rel="stylesheet" href="./bootstrap.min.css">
</head>
<body>
  <div class="container>
<h1 class="text-center">ACL 2024 Overview</h1>
<hr>

ACL 2024 main conference录用率为940/4407=21.3%，相比ACL 2023的录用率1074/4864=22.08%整体持平。

## Part One: Tutorial

今年tutorial共有6个，分别是：

#### tutorial 1 Computational Linguistics for Brain Encoding and Decoding: Principles, Practices and Beyond

近年来，计算语言学（CL）取得了巨大进展，大型语言模型等模型在自然语言处理任务中表现出色，凸显了其有助于理解大脑语言处理的潜力，特别是从大脑编码和解码的角度。大脑编码涉及将语言刺激映射到大脑活动中，而大脑解码则是从观察到的大脑活动中重建语言刺激。擅长捕捉和操纵语言特征的CL模型对于语言刺激与大脑活动的相互映射至关重要。大脑编码和解码具有广泛应用，包括增强人机交互和为沟通障碍者开发辅助技术等。本教程将重点阐述计算语言学如何促进大脑编码和解码，深入探讨其原则和实践方法，并讨论面临的挑战及未来方向。通过此教程，旨在为计算语言学与认知神经科学交叉领域提供全面且信息丰富的概览，激发该领域未来研究的热情。

#### tutorial 2 Automatic and Human-AI Interactive Text Generation (with a focus on Text Simplification and Revision)

本教程专注于文本到文本的生成，这是一种自然语言生成（NLG）任务，它接受一段文本作为输入，并根据特定标准（如可读性或语言风格）生成改进后的修订版，同时大致保留原文的意义和长度。这包括文本简化、释义生成、风格转换等多种应用。与文本摘要和开放式文本补全（如故事创作）相比，本教程讨论的文本到文本生成任务在语义一致性和目标语言风格上更为受限，这种控制水平使其成为研究模型生成既语义恰当又风格合适的文本能力的理想测试平台。此外，这些任务从技术角度来看也很有趣，因为它们需要词汇和句法转换、风格控制和遵守事实知识的复杂组合。本教程特别关注文本简化和修订，旨在从数据、模型、人机协作和评估四个方面概述最新的自然语言生成研究，并讨论和展示几项重要和最近的进展，包括非回溯方法的使用、从大规模语言模型的微调转向提示、新的可学习指标和细粒度人工评估框架的开发、非英语语言研究和数据集的增多，以及HCI+NLP+可访问性跨学科研究的兴起，以创建现实世界的写作辅助系统。

#### tutorial 3 Computational Expressivity of Neural Language Models

本教程旨在通过形式语言理论（FLT）的工具，为现代语言模型（LMs）的正式分析提供一个全面的框架介绍，以激励对LMs能力和局限性的更好理论表征。尽管LMs在NLP研究中展现出卓越的多任务适应性，但其观察到的能力与现有正式机制提出的解释之间存在较大差距。本教程将展示FLT工具如何有助于理解现代神经网络LM架构的内部工作机制并预测其能力。我们将涵盖使用FLT对基于循环神经网络和Transformer的LMs进行精确且实际相关的陈述的最新成果，将它们与有限状态自动机、图灵机和模拟电路等形式设备相关联。总的来说，本教程中的结果将使我们能够对LMs的观测和预测行为进行精确陈述和解释，并为架构中可以改进的方面提供理论上的建议。

#### tutorial 4 Presentation Matters: How to Communicate Science in the NLP Venues and in the Wild?

每年有大量早期职业研究者加入NLP/计算语言学界，他们通常从在ACL会议和研讨会上展示研究成果开始。然而，除了撰写论文这一重要步骤外，如何有效地传达研究成果同样重要，它决定了研究成果的影响力。此外，并非所有博士生都有机会接受演讲技巧的培训，研究方法课程的质量参差不齐，可能不涉及科学交流，也绝非全部针对NLP社区量身定制。因此，我们提议开设一门介绍性教程，涵盖写作、口头报告（海报和演示）以及社交媒体存在等多种沟通技巧，以弥补那些可能无法接触到研究方法课程或其他导师帮助的研究者在这方面的不足。这种互动式教程将允许参与者提问和澄清，这是仅通过阅读材料无法实现的。

#### tutorial 5 Vulnerabilities of Large Language Models to Adversarial Attacks

本教程是关于大型语言模型（LLMs）对抗性攻击漏洞的综合性指南，这是一个融合了自然语言处理（NLP）和网络安全观点的跨学科领域。随着LLMs日益复杂并融入各种系统，了解其安全属性至关重要。然而，当前研究表明，即使是注重安全性的模型也无法完全抵御可能导致错误或有害输出的对抗性攻击。教程首先介绍注重安全性的LLMs和网络安全概念，奠定基础。随后，根据不同学习架构和攻击方法对现有研究进行分类。重点分析了单模态LLMs、多模态LLMs以及集成LLMs系统的现有漏洞，特别是旨在利用弱点并误导AI系统的对抗性攻击。最后，教程深入探讨了这些漏洞的潜在原因，并讨论了潜在的防御机制。

#### tutorial 6 Watermarking for Large Language Model

随着AI生成文本日益接近人类撰写内容，检测机器生成文本的能力在计算语言学和机器学习领域变得至关重要。本教程旨在深入探索文本水印技术，这是语言隐写术的一个子领域，旨在将隐藏信息（水印）嵌入文本段落中。我们将介绍文本水印的基础知识，讨论识别AI生成文本的主要挑战，并深入研究当前的水印方法，评估其优缺点。此外，我们还将探讨文本水印的其他可能应用，并讨论该领域的未来发展方向。每个部分都将通过示例和关键点进行补充。

## Part Two: Topic

基于个人比较感兴趣的几个方向，整理了几篇论文。

### Basic Theory & Mechanism

###### The Heuristic Core: Understanding Subnetwork Generalization in Pretrained Language Models

先前的研究发现，使用不同随机种子微调的预训练语言模型（LMs）可以实现相似的域内性能，但在句法泛化测试中表现出不同的泛化能力。在本文中，我们展示了即使在单个模型内部，我们也可以找到多个在域内表现相似但泛化能力截然不同的子网络。为了更好地理解这些现象，我们研究了它们是否可以从“竞争子网络”的角度来理解：模型最初代表多种不同的算法，对应于不同的子网络，当最终收敛到一种算法时，就会发生泛化。这种解释已被用于解释简单算法任务（“grokking”）中的泛化现象。我们没有发现竞争子网络，而是发现所有子网络（无论是否泛化）都共享一组注意力头，我们称之为启发式核心。进一步的分析表明，这些注意力头在训练早期就会出现，并计算浅层的、非泛化的特征。模型通过引入额外的注意力头来学习泛化，这些注意力头依赖于“启发式”头的输出来计算更高级别的特征。总的来说，我们的研究结果为预训练LMs中的句法泛化机制提供了更详细的图景。

###### The Probabilities Also Matter: A More Faithful Metric for Faithfulness of Free-Text Explanations in Large Language Models

为了监督先进的人工智能系统，了解它们生成特定输出的原因至关重要。在提示下，大型语言模型（LLM）可以提供听起来合理且获得人类注释者高评分的自然语言解释或推理轨迹。然而，尚不清楚这些解释在多大程度上真正捕捉到了模型预测所依赖的因素：最“人性化”的解释可能与最忠实于模型真实决策过程的解释不同。在这项工作中，我们介绍了相关性反事实测试（CCT），这是一种基于反事实输入编辑的忠实度度量标准，它不仅考虑了二元标签的变化，还考虑了模型预测标签分布的总变化。我们在三项自然语言处理任务上评估了来自Llama-2系列模型在少量提示下生成的自由文本解释的忠实度。我们发现，当这些因素对模型的预测有影响时，这些解释确实更有可能提及它们，关联程度随着模型规模的增加而增加，但不同任务之间的变化很大。

### alignment/hallucination

###### Back to Basics: Revisiting REINFORCE-Style Optimization for Learning from Human Feedback in LLMs

以人类反馈强化学习（RLHF）形式出现的人工智能对齐正日益被视为高性能大型语言模型（LLMs）的关键要素。近端策略优化（PPO）已被开创性文献确立为RLHF中强化学习（RL）部分的标准方法。然而，它涉及高昂的计算成本和敏感的超参数调整。我们认为，导致PPO发展的大多数动机原则在RLHF中并不是实际关注的重点，并主张采用一种计算成本更低且能保持甚至提高性能的方法。我们重新审视了在RL背景下，如何根据人类偏好进行对齐。以简单性为指导原则，我们表明，在RLHF的上下文中，PPO的许多组件都是不必要的，而且远比其简单的REINFORCE风格的优化变体在性能上优于PPO和新提出的“无RL”方法，如DPO和RAFT。我们的工作表明，通过仔细适应LLMs对齐特性，可以以低成本从在线RL优化中获益。

###### TruthX: Alleviating Hallucinations by Editing Large Language Models in Truthful Space

大型语言模型（LLM）有时会出现产生幻觉的情况，尤其是尽管知道正确答案，但LLM仍可能生成不真实的回答。激活LLM内部的真实性是充分发挥其知识潜力的关键。在本文中，我们提出了TruthX，这是一种在推理时通过识别和编辑LLM内部表示中控制真实性的特征来激活LLM真实性的干预方法。TruthX采用自编码器将LLM的表示分别映射到语义和真实性的潜在空间，并应用对比学习在真实性空间内确定一个真实的编辑方向。在推理过程中，通过编辑LLM在真实性空间内的内部表示，TruthX有效增强了LLM的真实性。实验表明，在TruthfulQA基准测试中，TruthX将13种先进LLM的真实性平均提高了20%。进一步的分析表明，TruthX仅通过编辑LLM内部表示中的一个向量，就可以控制LLM生成真实或幻觉的回答。

### long context

###### ∞Bench: Extending Long Context Evaluation Beyond 100K Tokens

处理和推理长上下文对于大型语言模型（LLMs）的许多实际应用至关重要，如文档理解和代理构建。尽管最近在使LLMs处理超过10万个标记的上下文方面取得了进展，但目前仍缺乏一个标准化的基准来评估这种长上下文能力。现有的公共基准通常关注大约1万个标记的上下文，这限制了在处理更长上下文时对LLMs的评估和比较。在本文中，我们提出了LongBench，这是第一个平均数据长度超过10万个标记的LLM基准。LongBench包括英语和中文中跨越不同领域的合成和真实任务。LongBench中的任务设计需要理解上下文中的长依赖关系，并且仅仅从上下文中检索有限数量的段落对于这些任务来说是不够的。基于LongBench，我们评估了几种专为处理长上下文而定制的最先进的LLMs。实验结果表明，现有的长上下文LLMs在处理10万个以上标记的上下文时仍需要显著的进步。此外，我们还就LLMs处理长上下文的行为提出了三项有趣的分析。我们的代码和数据已发布。

###### Long-Context Language Modeling with Parallel Context Encoding

将大型语言模型（LLMs）扩展到处理更长的输入对于广泛的应用至关重要。然而，Transformer的巨大计算成本和位置编码的有限泛化能力限制了其上下文窗口的大小。我们引入了并行编码的上下文扩展（CEPE）框架，该框架可以应用于任何现有的仅解码器LLMs，以扩展其上下文窗口。CEPE采用一个小型编码器逐块处理长输入，使冻结的解码器能够通过交叉注意力利用额外的上下文。CEPE高效、通用且灵活：使用8K标记的文档进行训练后，它将LLAMA-2的上下文窗口扩展到128K标记，吞吐量提高了10倍，而内存仅为原来的1/6。CEPE在语言建模和上下文学习方面表现出色。同时，在检索增强的应用中，CEPE也表现出色，而现有的长上下文模型在检索到的上下文中会退化。我们还介绍了一种CEPE变体，它仅使用未标记数据就可以扩展指令调优模型的上下文窗口，并在LLAMA-2-CHAT上展示了其有效性，从而构建了一个强大的指令遵循模型，该模型可以在下游任务中利用非常长的上下文。

### LoRA

###### AFLoRA: Adaptive Freezing of Low Rank Adaptation in Parameter Efficient Fine-Tuning of Large Models

我们提出了一种新颖的参数高效微调（PEFT）方法，称为低秩适应自适应冻结（AFLoRA）。具体而言，对于每个预训练好的冻结权重张量，我们增加了一条可训练的低秩矩阵并行路径，即一个下投影矩阵和一个上投影矩阵，每个矩阵后都跟着一个特征变换向量。基于一种新颖的冻结分数，我们在微调过程中逐步冻结这些投影矩阵，以减少计算量并缓解过拟合问题。我们的实验结果表明，在GLUE基准测试中，我们的方法能够以平均高达0.85%的改进达到最先进的性能，同时产生的平均可训练参数数量减少了高达9.5倍。在运行时方面，与类似的PEFT替代方案相比，AFLoRA可以带来高达1.86倍的性能提升。除了我们方法的实用性之外，我们还就不同模块中LoRA路径的训练性要求以及不同投影矩阵的冻结计划提供了见解。

###### LoRA-Flow: Dynamic LoRA Fusion for Large Language Models in Generative Tasks

LoRA 采用轻量级模块为每个下游任务或领域定制大型语言模型（LLMs），其中不同的学习附加模块代表不同的技能。将现有的 LoRA 结合起来以应对新任务可以增强已学习 LoRA 的可重用性，这对标注数据有限的任务尤其有益。关于 LoRA 组合的大部分先前工作主要依赖于每个参与 LoRA 的任务级权重，导致不同的示例和标记共享相同的 LoRA 权重。然而，在生成任务中，不同的标记可能需要不同的技能来处理。以中文数学任务为例，理解问题描述可能更多地依赖于中文 LoRA，而计算部分则可能更多地依赖于数学 LoRA。为此，我们提出了 LoRA-Flow，它利用动态权重来调整不同 LoRA 的影响。每个步骤的权重由参数极少的融合门确定，该融合门仅通过 200 个训练示例即可学习。在六个生成任务上的实验表明，我们的方法始终优于具有任务级融合权重的基线方法。这强调了为 LoRA 组合引入动态融合权重的必要性。

###### LoRAMoE: Alleviating World Knowledge Forgetting in Large Language Models via MoE-Style Plugin

监督微调（SFT）是大型语言模型（LLM）的关键步骤，它使模型能够与人类指令保持一致，并增强其在下游任务中的能力。大幅增加指令数据是使模型与更广泛的下游任务保持一致或显著提高其在特定任务上性能的直接解决方案。然而，我们发现，指令数据的大规模增加可能会损害LLM中先前存储的世界知识。为了解决这一挑战，我们提出了LoRAMoE，这是一个新颖的框架，它引入了多个低秩适配器（LoRA），并使用路由器网络（类似于专家混合（MoE）的插件版本）将它们集成在一起。该框架冻结了主干模型，并迫使一部分LoRA专注于利用世界知识来解决下游任务，从而缓解世界知识边缘遗忘的问题。实验结果表明，随着指令数据的增加，LoRAMoE可以显著提高处理下游任务的能力，同时保持LLM中存储的世界知识。

### Agent

###### Tell Me More! Towards Implicit User Intention Understanding of Language Model Driven Agents

当前基于语言模型的代理往往缺乏有效的用户参与机制，这在用户指令通常含糊不清的情况下至关重要。尽管这些代理擅长制定策略和执行任务，但它们在寻求澄清和把握用户精确意图方面存在困难。为了弥补这一差距，我们引入了“交互中的意图”（IN3），这是一个旨在通过显式查询来检查用户隐式意图的新型基准。接下来，我们提出在代理设计中将模型专家作为上游部分，以增强用户与代理之间的交互。利用IN3，我们实证性地训练了Mistral-Interact，这是一个强大的模型，它能够主动评估任务的模糊性，询问用户意图，并在开始下游代理任务执行之前将其细化为可操作的目标。我们将其集成到XAgent框架中，对增强的代理系统在用户指令理解和执行方面进行了全面评估，结果表明我们的方法在识别模糊的用户任务、恢复和总结关键缺失信息、设置精确且必要的代理执行目标以及最小化冗余工具使用方面表现出色，从而提高了整体效率。

### RAG

###### Unsupervised Information Refinement Training of Large Language Models for Retrieval-Augmented Generation

检索增强生成（RAG）通过整合检索到的额外信息来增强大型语言模型（LLMs）的性能。然而，研究表明，LLMs在有效利用检索到的信息方面仍面临挑战，甚至可能忽视这些信息或被其误导。主要原因是LLMs的训练没有明确让LLMs学会如何利用质量参差不齐的检索文本作为输入。在本文中，我们提出了一种新的视角，将LLMs在RAG中的角色视为“信息精炼器”，这意味着无论检索到的文本的正确性、完整性或有用性如何，LLMs都能持续地将检索文本中的知识与模型参数相结合，生成比检索文本更简洁、准确和完整的文本。为此，我们提出了一种名为INFO-RAG的信息精炼训练方法，该方法以无监督的方式优化用于RAG的LLMs。INFO-RAG成本低廉，适用于各种任务。在包括问答、槽位填充、语言建模、对话和代码生成在内的多样化任务的11个数据集上进行的零样本预测广泛实验表明，INFO-RAG将LLaMA2的性能平均提高了9.39%的相对点。INFO-RAG还展示了在RAG的上下文学习和鲁棒性方面的优势。

</div>
</body>
<!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
<script src="https://fastly.jsdelivr.net/npm/jquery@1.12.4/dist/jquery.min.js"
integrity="sha384-nvAa0+6Qg9clwYCGGPpDQLVpLNn0fRaROjHqs13t4Ggj3Ez50XnGQqc/r8MhnRDZ"
crossorigin="anonymous"></script>
<!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
<!-- <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"
integrity="sha384-aJ21OjlMXNL5UyIl/XNwTMqvzeRMZH2w8c5cRVpzpU8Y5bApTppSuUkhZXN0VxHd"
crossorigin="anonymous"></script> -->
<!-- <script>
document.addEventListener("DOMContentLoaded", function () {
    renderMathInElement(document.body, {
        // customised options
        // • auto-render specific keys, e.g.:
        delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\(', right: '\\)', display: false },
            { left: '\\[', right: '\\]', display: true }
        ],
        // • rendering keys, e.g.:
        throwOnError: false
    });
});
</script> -->
</html>
