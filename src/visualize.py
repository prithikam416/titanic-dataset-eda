"""
visualize.py - Charts and Visualization module for Titanic EDA
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

OUTPUT_DIR = "output/charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Visual styling
plt.style.use('dark_background')
plt.rcParams.update({
    'figure.facecolor': '#1e1e24',
    'axes.facecolor':   '#111116',
    'font.family':      'sans-serif',
    'axes.spines.top':  False,
    'axes.spines.right':False,
})

def plot_survival_ratio(df, save=True):
    """Plot simple pie chart of survival ratio."""
    counts = df['Survived'].value_counts()
    labels = ['Did Not Survive', 'Survived']
    colors = ['#e74c3c', '#2ecc71']
    
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='#1e1e24')
    ax.pie(
        counts,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        wedgeprops=dict(edgecolor='white', linewidth=1.5),
        textprops={'color': 'white', 'fontsize': 12, 'fontweight': 'bold'}
    )
    ax.set_title('Overall Passenger Survival Ratio', fontsize=14, fontweight='bold', color='white', pad=20)
    plt.tight_layout()
    if save:
        plt.savefig(f"{OUTPUT_DIR}/survival_ratio.png", dpi=150, bbox_inches='tight')
        print(f"[INFO] Saved chart: {OUTPUT_DIR}/survival_ratio.png")
    plt.show()

def plot_survival_by_gender(df, save=True):
    """Plot survival rate comparison by sex."""
    fig, ax = plt.subplots(figsize=(7, 5), facecolor='#1e1e24')
    ax.set_facecolor('#111116')
    
    sns.barplot(x='Sex', y='Survived', data=df, errorbar=None, palette=['#3498db', '#e84393'], ax=ax, edgecolor='white')
    
    ax.set_title('Survival Rate by Gender', fontsize=14, fontweight='bold', color='white', pad=15)
    ax.set_xlabel('Sex', fontsize=12)
    ax.set_ylabel('Survival Rate (0 to 1)', fontsize=12)
    
    # Add values on top of bars
    for p in ax.patches:
        ax.annotate(f"{p.get_height()*100:.1f}%", (p.get_x() + p.get_width() / 2., p.get_height() - 0.08),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                    color='white', fontsize=12, fontweight='bold')
                    
    plt.tight_layout()
    if save:
        plt.savefig(f"{OUTPUT_DIR}/survival_by_gender.png", dpi=150, bbox_inches='tight')
        print(f"[INFO] Saved chart: {OUTPUT_DIR}/survival_by_gender.png")
    plt.show()

def plot_survival_by_class(df, save=True):
    """Plot survival rate comparison by passenger class."""
    fig, ax = plt.subplots(figsize=(7, 5), facecolor='#1e1e24')
    ax.set_facecolor('#111116')
    
    sns.barplot(x='Pclass', y='Survived', data=df, errorbar=None, palette='viridis', ax=ax, edgecolor='white')
    
    ax.set_title('Survival Rate by Passenger Class (Pclass)', fontsize=14, fontweight='bold', color='white', pad=15)
    ax.set_xlabel('Pclass (1 = Upper, 2 = Middle, 3 = Lower)', fontsize=12)
    ax.set_ylabel('Survival Rate', fontsize=12)
    
    for p in ax.patches:
        ax.annotate(f"{p.get_height()*100:.1f}%", (p.get_x() + p.get_width() / 2., p.get_height() - 0.08),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                    color='white', fontsize=12, fontweight='bold')
                    
    plt.tight_layout()
    if save:
        plt.savefig(f"{OUTPUT_DIR}/survival_by_class.png", dpi=150, bbox_inches='tight')
        print(f"[INFO] Saved chart: {OUTPUT_DIR}/survival_by_class.png")
    plt.show()

def plot_age_distribution(df, save=True):
    """Plot age distribution density of survivors vs non-survivors."""
    fig, ax = plt.subplots(figsize=(9, 5), facecolor='#1e1e24')
    ax.set_facecolor('#111116')
    
    sns.kdeplot(df[df['Survived'] == 1]['Age'], label='Survived', fill=True, color='#2ecc71', alpha=0.4, ax=ax)
    sns.kdeplot(df[df['Survived'] == 0]['Age'], label='Did Not Survive', fill=True, color='#e74c3c', alpha=0.4, ax=ax)
    
    ax.set_title('Passenger Age Distribution by Survival Status', fontsize=14, fontweight='bold', color='white', pad=15)
    ax.set_xlabel('Age (Years)', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.legend(facecolor='#111116', labelcolor='white')
    
    plt.tight_layout()
    if save:
        plt.savefig(f"{OUTPUT_DIR}/age_distribution.png", dpi=150, bbox_inches='tight')
        print(f"[INFO] Saved chart: {OUTPUT_DIR}/age_distribution.png")
    plt.show()

def plot_correlation_heatmap(df, save=True):
    """Plot correlation heatmap for numeric values."""
    fig, ax = plt.subplots(figsize=(8, 6), facecolor='#1e1e24')
    
    # Filter to numeric columns only
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    
    sns.heatmap(
        corr_matrix, 
        annot=True, 
        cmap='coolwarm', 
        fmt=".2f", 
        linewidths=.5, 
        ax=ax, 
        annot_kws={'fontsize':10, 'weight':'bold'}
    )
    ax.set_title('Correlation Matrix of Numeric Features', fontsize=14, fontweight='bold', color='white', pad=15)
    ax.tick_params(colors='white')
    
    plt.tight_layout()
    if save:
        plt.savefig(f"{OUTPUT_DIR}/correlation_heatmap.png", dpi=150, bbox_inches='tight')
        print(f"[INFO] Saved chart: {OUTPUT_DIR}/correlation_heatmap.png")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("data/titanic_cleaned.csv")
    plot_survival_ratio(df)
    plot_survival_by_gender(df)
    plot_survival_by_class(df)
    plot_age_distribution(df)
    plot_correlation_heatmap(df)
