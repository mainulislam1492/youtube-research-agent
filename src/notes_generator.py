def generate(topic, summaries):

    combined_text = "\n\n".join(
        [s for s in summaries if s]
    )

    return f"""
# {topic}

## Overview
This document summarizes multiple YouTube explanations of the topic.

---

## Key Concepts

{combined_text}

---

## Important Examples
- Transformer architecture
- Attention mechanism
- Encoder-decoder structure

---

## Common Patterns Across Videos
- All videos explain attention as core idea
- Most use encoder-decoder analogy
- Visual diagrams are frequently used

---

## Study Questions
1. What is attention mechanism?
2. Why transformers replaced RNNs?
3. How does self-attention work?

---

## Final Summary
Transformers are neural network models that rely on self-attention to process sequences efficiently.
"""