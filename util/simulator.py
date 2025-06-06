from util.collision import check_wall_collision, check_particle_collision


def step(particles, dt):
    # 位置更新
    for p in particles:
        p.update(dt)

    # 壁衝突処理
    for p in particles:
        check_wall_collision(p, box_size=1.0)

    # 粒子間衝突（全組み合わせ）
    n = len(particles)
    for i in range(n):
        for j in range(i + 1, n):
            check_particle_collision(particles[i], particles[j])
