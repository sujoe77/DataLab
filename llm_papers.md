# LLM papers

From ChatGPT

If your goal is to understand today's LLMs

A progression often recommended in Stanford NLP circles is:

    A Neural Probabilistic Language Model (Yoshua Bengio, 2003)
    Distributed Representations of Words and Phrases and their Compositionality (word2Vec, google, 1310.4546)
    Seq2Seq + Attention (google, 2014–2015)
    Attention Is All You Need (Transformer, google 2017)
    BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (BERT, 2018)
    Language Models are Unsupervised Multitask Learners (GPT2, 2019)
    Scaling Laws for Neural Language Models (OpenAI 2020)
    Training Compute-Optimal Large Language Models (google, 2022)
    A Comprehensive Overview of Large Language Models (multiple universities, 2023)

This sequence gives a coherent historical path from Bengio's learned word embeddings (which you asked about earlier) to modern Transformer-based language models.

## Papers

### NNLM

by Yoshua Bengio, 2003

[A Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)

> A very popular model architecture for estimating neural network language model (NNLM) was proposed in [1], where a feedforward neural network with a linear projection layer and a non-linear hidden layer was used to learn jointly the word vector representation and a statistical language model. This work has been followed by many others.

### Word2Vec + Distributed Representations of Words and Phrases 2013

embedding algo

Wiki: <https://en.wikipedia.org/wiki/Word2vec>

Paper: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)
       [Distributed Representations of Words and Phrases and their Compositionality (1310.4546)](https://arxiv.org/abs/1310.4546)

We propose two novel model architectures for **computing continuous vector representations** of words from very large data sets. The quality of these representations is measured in a word similarity task, and the results are compared to the previously best performing techniques based on different types of neural networks. We observe **large improvements in accuracy at much lower computational cost**, i.e. it takes less than a day to learn high quality word vectors from a 1.6 billion words data set. Furthermore, we show that these vectors provide state-of-the-art performance on our test set for measuring syntactic and semantic word similarities.

### Seq2Seq + Attention 2014

introduced attention

[Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)

see also: <https://en.wikipedia.org/wiki/Seq2seq>

> Seq2seq is a family of machine learning approaches used for natural language processing.[1] Originally developed by Lê Viết Quốc, a Vietnamese computer scientist and a machine learning pioneer at Google Brain, this framework has become foundational in many modern AI systems. Applications include language translation,[2] image captioning,[3] conversational models,[4] speech recognition,[5] and text summarization.[6] Seq2seq uses sequence transformation: it turns one sequence into another sequence.

[Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473)

> Neural machine translation is a recently proposed approach to machine translation. Unlike the traditional statistical machine translation, the neural machine translation aims at building a single neural network that can be jointly tuned to maximize the translation performance. The models proposed recently for neural machine translation often belong to a family of encoder-decoders and consists of an encoder that encodes a source sentence into a fixed-length vector from which a decoder generates a translation. In this paper, we conjecture that the use of a fixed-length vector is a bottleneck in improving the performance of this basic encoder-decoder architecture, and propose to extend this by allowing a model to automatically **(soft-)search for parts** of a source sentence that are **relevant** to predicting a target word, without having to form these parts as a hard segment explicitly. With this new approach, we achieve a translation performance comparable to the existing state-of-the-art phrase-based system on the task of English-to-French translation. Furthermore, qualitative analysis reveals that the (soft-)alignments found by the model agree well with our intuition.

### Transformer 2017

from RNN, CNN to attention

[Attention Is All You Need](https://arxiv.org/abs/1706.03762)

wiki: <https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)>

> The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the **Transformer**, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the **WMT 2014 English-to-German** translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the **WMT 2014 English-to-French** translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

see also: [Transformer论文逐段精读](https://www.youtube.com/watch?v=nzqlFIcCSWQ&t=55s)

    00:00 标题和作者
    03:21 摘要
    08:11 结论
    10:05 导言
    14:35 相关工作
    16:34 模型
        33:39 3.2 attention
        35:55 3.2.1 scaled dot product attention
        44:10 3.2.2 multi-head
        47:50 3.2.3 applications of attention
        
    1:12:49 实验
    1:21:46 讨论

    Architecture

        [MLP](https://en.wikipedia.org/wiki/Multilayer_perceptron)

        [residual connection](https://en.wikipedia.org/wiki/Residual_neural_network)

    mentioned papers

        斯坦福提出“基础模型”（Foundation Model）的开山之作，是其以人为中心人工智能研究院（Stanford HAI）于2021年8月发布的重磅长篇论文。

            https://crfm.stanford.edu/assets/report.pdf

        ResNet https://arxiv.org/abs/1512.03385

see also: [Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!](https://www.youtube.com/watch?v=zxQyTK8quyY)

### BERT 2018

pre-trained model for multiple tasks.

[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://research.google/pubs/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/)

wiki: <https://en.wikipedia.org/wiki/BERT_(language_model)>

> We introduce a new language representation model called BERT, which stands for **Bidirectional Encoder Representations from Transformers**. Unlike recent language representation models, BERT is designed to **pre-train deep bidirectional representations** from unlabeled text by jointly conditioning on both left and right context in all layers. As a result, the pre-trained BERT model can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.
>BERT is conceptually simple and empirically powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the **GLUE** score to 80.5% (7.7% point absolute improvement), **MultiNLI** accuracy to 86.7% (4.6% absolute improvement), **SQuAD** v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) and **SQuAD v2.0** Test F1 to 83.1 (5.1 point absolute improvement).

see also: [Encoder-Only Transformers (like BERT) for RAG, Clearly Explained!!!](https://www.youtube.com/watch?v=GDN649X_acE)

    Encode only (BERT) vs Decoder Only (for chapGpt)

### GPT2 - OpenAI 2019

[Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

> "Language Models are Unsupervised Multitask Learners" is the title of the landmark February 2019 research paper by OpenAI that introduced GPT-2. Authored by Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever, this paper shifted the artificial intelligence paradigm away **from training narrow, task-specific models with supervised data toward building generalist foundation models** via massive next-token prediction.

### Scaling Laws for Neural Language Models (OpenAI 2020)

[Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361)

> The foundational OpenAI Scaling Laws paper introduced several critical principles for building large language models:
>
> * Scale Over Shape: Modifying the aspect ratio, width, or depth of a transformer yields very little variation in validation loss. Focus instead on raw scaling.
> * Sample Efficiency: Larger models extract more information from the same number of data tokens than smaller models. They reach the same target loss in fewer optimization steps.
> * Early Stopping is Optimal: If you operate under a rigid compute ceiling, the most efficient route is to train massive models on modest datasets. It is more efficient to stop long before full convergence rather than training a small model to its absolute limit.Overfitting Lower Bound:
> * Overfitting occurs if your dataset size does not grow alongside model capacity. To maintain equivalent training efficiency without overfitting, an increase of 10× in model size (N) requires a corresponding 5.5× expansion of dataset size (D)

### Training Compute-Optimal Large Language Models

[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)

> "Training Compute-Optimal Large Language Models" is a seminal 2022 research paper published by Google DeepMind that fundamentally reshaped how the AI community approaches the scaling of artificial intelligence.

### Modern LLM papers (GPT-4, Llama, DeepSeek, Claude, etc.) - multiple universities, 2023

[A Comprehensive Overview of Large Language Models](https://arxiv.org/abs/2307.06435)

>a concise yet comprehensive overview of the recent developments in this field. This article provides an **overview of the literature on a broad range of LLM-related concepts**. Our self-contained comprehensive overview of LLMs discusses relevant **background concepts** along with covering the **advanced topics** at the frontier of research in LLMs. This review article is intended to provide not only a systematic survey but also a **quick, comprehensive reference** for the researchers and practitioners to draw insights from extensive, informative summaries of the existing works to advance the LLM research.

## Videos

understanding LLM

    https://www.youtube.com/watch?v=bOlVx5zeHLM

    from: https://www.understandingai.org/p/large-language-models-explained-with

## Terms

* Tokenization <https://en.wikipedia.org/wiki/Large_language_model#Tokenization>
* Embedding <https://en.wikipedia.org/wiki/Word_embedding>
* Attention <https://en.wikipedia.org/wiki/Attention_(machine_learning)#cite_note-wang2014-12>

## Models

transformer based models - 2023

![](https://amatria.in/blog/images/02-06.png)

# Ref

[Resnet](https://arxiv.org/abs/1512.03385) 