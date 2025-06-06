import os
import csv
from util.particle import Particle
from util.simulator import step as sim_step
from draw.renderer import render
from PIL import Image


def load_particles(csv_path):
    particles = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            p = Particle(
                pid=i,
                x=float(row["x_pos"]),
                y=float(row["y_pos"]),
                vx=float(row["x_vel"]),
                vy=float(row["y_vel"]),
            )
            particles.append(p)
    return particles


def save_positions(particles, step, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    raw_dir = os.path.join(output_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    csv_path = os.path.join(raw_dir, f"step_{step:04d}.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["particle_id", "x", "y", "vx", "vy", "collision_count"])
        for p in particles:
            writer.writerow([p.id, p.x, p.y, p.vx, p.vy, p.collision_count])


def create_gif(image_paths, output_path):
    images = [Image.open(path) for path in image_paths]
    images[0].save(
        output_path, save_all=True, append_images=images[1:], duration=100, loop=0
    )


def simulate(particles, steps=100, dt=0.01):
    output_data_dir = "data/output"
    temp_image_dir = os.path.join(output_data_dir, "temp_images")
    gif_path = os.path.join(output_data_dir, "simulation.gif")
    image_paths = []

    for t in range(steps):
        sim_step(particles, dt)

        if t % 10 == 0:
            save_positions(particles, t, output_data_dir)
            render(particles, t, temp_image_dir, image_paths)

    create_gif(image_paths, gif_path)

    # 中間画像を削除
    for path in image_paths:
        os.remove(path)
    os.rmdir(temp_image_dir)


if __name__ == "__main__":
    input_path = "data/input/input.csv"
    particles = load_particles(input_path)
    print(f"Loaded {len(particles)} particles from {input_path}")

    print("Starting simulation...")
    simulate(particles, steps=2500, dt=0.0025)
    print("Simulation completed. Output saved to 'data/output/simulation.gif'.")
