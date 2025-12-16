# Recursive Image Analysis Research

<p align="center">
  <img src="images/000.png" width="30%" alt="First İmage" style="vertical-align: middle;"/>
  <img src="https://www.pngall.com/wp-content/uploads/13/White-Arrow-PNG-Pic-300x161.png" width="30%" margin-bottom="30px" style="vertical-align: middle;"/>
  <img src="images/101.png" width="30%" alt="Last İmage" style="vertical-align: middle;"/>
</p>

## Overview
What happens when you ask a Generative AI to edit an image but tell it to **"change nothing"**?

This project investigates the inherent biases, degradation patterns, and "hallucinations" of AI image generation models when subjected to a recursive loop with zero instructions. By feeding the output of one generation back as the input for the next—while explicitly commanding the AI to make no consistency changes—we reveal the underlying tendencies of the model.

Does the image stay the same? Does it degrade into noise? Or does it evolve into something specific?

You can download the full version of the dataset I used from [this link](https://drive.google.com/drive/folders/13KeW2_PczrjyBfnNsrJTQqgIK7yWnwF-?usp=sharing).

## Methodology
The experiment follows a strict recursive loop:
1.  **Input:** Start with an initial seed image.
2.  **Process:** Pass the image to an AI Image-to-Image generator.
3.  **Prompt:** The prompt is systematically set to a null-instruction (e.g., "Change nothing", "Same image", "High quality").
4.  **Loop:** The resulting output image becomes the *input* for the next iteration.
5.  **Repeat:** This cycle is repeated 100+ times.

## Key Visualizations & Interpretation

### 1. Structural Similarity (SSIM)
![SSIM Graph](graphs/ssim.png)

**Interpretation:**
*   **Rapid Divergence:** The sharp initial drop (~0.35) against the original image shows that the model *cannot* truly "change nothing." Even with a null prompt, it re-encodes and re-imagines the image significantly in the first few steps.
*   **Local Stability:** The high "To Previous" score (~0.90) indicates the model is consistent in its drift. It doesn't make wild jumps; it slowly morphs the image, step-by-step, down a specific path.

### 2. Information Content (Entropy)
![Entropy Graph](graphs/entropy.png)

**Interpretation:**
*   **Simplification:** We observe a massive drop in entropy (from ~-200 to ~-1350).
*   **Smoothing Effect:** The model acts like a low-pass filter over time. It removes high-frequency noise, complex textures, and subtle details, preferring smooth, uniform, and "clean" areas. The AI "hallucinates" simplicity where there was once complexity.

### 3. Edge Density
![Edges Graph](graphs/edges.png)

**Interpretation:**
*   **Loss of Detail:** Confirming the entropy data, the number of edges decreases. The image becomes less detailed and more abstract/cartoony as the recursion progresses.

### 4. Color Drift ("The Green Shift")
![Color Drift Graph](graphs/color_drift.png)

**Interpretation:**
*   **The Model's Bias:** Without instruction, the model drifts towards specific parts of the color spectrum.
    *   **Green:** Significantly increases ($92 \to 114$).
    *   **Blue:** Significantly decreases ($80 \to 54$).
*   **Conclusion:** This specific model/setting has a "cool/green" bias. When left to its own devices, it slowly tints the world green and removes blue, likely due to the training data distribution or compression artifacts being amplified.

### 5. SSCI (Stability-to-Change Index)
![SSCI Graph](graphs/ssci.png)

**Interpretation:**
*   This metric highlights that while the image drifts far from the original, it reaches a state of "stable decay," where the rate of change slows down as it settles into the model's preferred visual minima.

## Research Findings
Based on 100+ recursive iterations, we conclude:

1.  **AI Cannot "Do Nothing":** Generative models are incapable of a perfect identity function. They always "dream" a little bit, adding or subtracting details based on their training.
2.  **Convergence to Simplicity:** The "hallucination" isn't chaotic; it's reductive. The model simplifies the world, removing noise and texture until only strong, simple shapes remain.
3.  **Deterministic Drift:** The degradation is directional. The "Green Shift" proves that the model has a preferred color palette that it gravitates towards when unconstrained.

## Usage
To replicate this analysis:

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Analysis:**
    Execute the Python scripts to analyze your own image sequences:
    ```bash
    python analysis_ssim.py
    python analysis_entropy.py
    python analysis_color_drift.py
    # ...
    ```

## Structure
- `images/`: Directory containing the recursive generation frames.
- `graphs/`: Generated visualization plots.
- `results/`: CSV data corresponding to the graphs.


