# Setting up Python

We'll cover this together in week 1. This page is here in case you want to do it early or need to set up again later.

[← Back to the course page](README.md)

## 1. Install Anaconda

Download Anaconda from [anaconda.com/download](https://www.anaconda.com/download) and install it with the default options. It comes with Python, Jupyter and most of the packages we use.

To check that it worked, open a terminal (on Windows, open **Anaconda Prompt**) and run:

```bash
python --version
```

You should see `Python 3.x.x`.

## 2. Create an environment for the course

An environment keeps the packages for this course separate from everything else on your computer.

```bash
conda create -n ibu060 python=3.12
conda activate ibu060
```

Run `conda activate ibu060` every time you open a new terminal to work on the course.

If you'd rather not use conda, a plain venv works too:

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

## 3. Start Jupyter

```bash
jupyter notebook
```

This opens a browser tab. Go to the folder where you cloned this repo and open any `.ipynb` file.

## 4. Get the course code

```bash
git clone https://github.com/MirzaKrupic/ibu060-2026.git
cd ibu060-2026
```

Before each class, run `git pull` to get the latest code.

## Something not working?

Come to lab or book a consultation (links are on the [course page](README.md#teaching-team)). Bring the full error message, or a screenshot of it.
