for i, node1 in enumerate(nodes):
    for node2 in nodes[i+1:]:
        nodes.sort(key=lambda node: node.x)

for i, node1 in enumerate(nodes):
    x1, y1 = node1.x, node1.y

    # Only check a window of nearby nodes in the sorted list
    for j in range(i + 1, min(i + 20, len(nodes))):
        node2 = nodes[j]
        x2, y2 = node2.x, node2.y

        dx = x1 - x2
        if dx * dx >= thresh:
            break  # nodes too far apart in x-direction

        dy = y1 - y2
        d_squared = dx * dx + dy * dy
        if d_squared < thresh:
            pygame.draw.aaline(
                screen, blue((thresh - d_squared) / thresh), (x1, y1), (x2, y2)
            )
   
