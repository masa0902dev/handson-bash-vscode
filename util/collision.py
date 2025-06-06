import math


def check_wall_collision(p, box_size):
    r = p.radius
    if p.x - r < 0 or p.x + r > box_size:
        p.vx *= -1
        p.collision_count += 1
    if p.y - r < 0 or p.y + r > box_size:
        p.vy *= -1
        p.collision_count += 1


def check_particle_collision(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.hypot(dx, dy)
    overlap = p1.radius + p2.radius - dist
    if overlap > 0:
        # 単純な2体の等質量弾性衝突モデル
        nx, ny = dx / dist, dy / dist
        dvx = p1.vx - p2.vx
        dvy = p1.vy - p2.vy
        dot = dvx * nx + dvy * ny

        if dot < 0:  # 近づいている場合のみ反射
            p1.vx -= dot * nx
            p1.vy -= dot * ny
            p2.vx += dot * nx
            p2.vy += dot * ny
            p1.collision_count += 1
            p2.collision_count += 1
