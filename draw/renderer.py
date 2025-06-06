import os
import matplotlib.pyplot as plt


def render(particles, step, output_dir, image_list, energy_threshold=0.15):
    os.makedirs(output_dir, exist_ok=True)

    xs = [p.x for p in particles]
    ys = [p.y for p in particles]

    # エネルギーに応じて色を決定（オレンジ: 高エネルギー, 青: 通常）
    colors = []
    for p in particles:
        speed_sq = p.vx**2 + p.vy**2
        kinetic_energy = 0.5 * speed_sq  # 質量1仮定
        if kinetic_energy >= energy_threshold:
            colors.append("orange")
        else:
            colors.append("blue")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(xs, ys, s=40, c=colors)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f"Step {step}")

    filename = os.path.join(output_dir, f"frame_{step:04d}.png")
    fig.savefig(filename)
    plt.close(fig)

    image_list.append(filename)
