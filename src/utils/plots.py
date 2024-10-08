import matplotlib.pyplot as plt


def plots(results):
    dfs_results = [result[0] for result in results]
    dfs_num_moves = [result["num_moves"] for result in dfs_results]
    dfs_max_open_size = [result["max_open_size"] for result in dfs_results]
    dfs_time = [result["time"].total_seconds() for result in dfs_results]

    if results[0][1] is None:
        bfs_num_moves = [0] * len(dfs_num_moves)
        bfs_max_open_size = [0] * len(dfs_num_moves)
        bfs_time = [0] * len(dfs_num_moves)
    else:
        bfs_results = [result[1] for result in results]
        bfs_num_moves = [result["num_moves"] for result in bfs_results]
        bfs_max_open_size = [result["max_open_size"] for result in bfs_results]
        bfs_time = [result["time"].total_seconds() for result in bfs_results]

    best_results = [result[2] for result in results]
    best_num_moves = [result["num_moves"] for result in best_results]
    best_max_open_size = [result["max_open_size"] for result in best_results]
    best_time = [result["time"].total_seconds() for result in best_results]

    _, axs = plt.subplots(1, 3, figsize=(12, 6))

    axs[0].plot(
        range(1, len(dfs_num_moves) + 1),
        dfs_num_moves,
        label="DFS - Number of Moves",
        color="b",
        marker="o",
    )
    axs[0].plot(
        range(1, len(bfs_num_moves) + 1),
        bfs_num_moves,
        label="BFS - Number of Moves",
        color="g",
        marker="x",
    )
    axs[0].plot(
        range(1, len(best_num_moves) + 1),
        best_num_moves,
        label="BestFS - Number of Moves",
        color="y",
        marker="s",
    )
    axs[0].set_title("Number of Moves Comparison")
    axs[0].set_xlabel("Game Instance")
    axs[0].set_ylabel("Number of Moves")
    axs[0].legend()
    axs[0].grid(True)

    axs[1].plot(
        range(1, len(dfs_max_open_size) + 1),
        dfs_max_open_size,
        label="DFS - Max Open Size",
        color="r",
        marker="o",
    )
    axs[1].plot(
        range(1, len(bfs_max_open_size) + 1),
        bfs_max_open_size,
        label="BFS - Max Open Size",
        color="orange",
        marker="x",
    )
    axs[1].plot(
        range(1, len(best_max_open_size) + 1),
        best_max_open_size,
        label="BestFS - Max Open Size",
        color="green",
        marker="s",
    )
    axs[1].set_title("Max Open Size Comparison")
    axs[1].set_xlabel("Game Instance")
    axs[1].set_ylabel("Max Open Size")
    axs[1].legend()
    axs[1].grid(True)

    axs[2].plot(
        range(1, len(dfs_time) + 1),
        dfs_time,
        label="DFS - Time",
        color="purple",
        marker="o",
    )
    axs[2].plot(
        range(1, len(bfs_time) + 1),
        bfs_time,
        label="BFS - Time",
        color="brown",
        marker="x",
    )
    axs[2].plot(
        range(1, len(best_time) + 1),
        best_time,
        label="BestFS - Time",
        color="black",
        marker="s",
    )
    axs[2].set_title("Time Comparison")
    axs[2].set_xlabel("Game Instance")
    axs[2].set_ylabel("Time (s)")
    axs[2].legend()
    axs[2].grid(True)

    plt.tight_layout()
    plt.title("Comparison of DFS, BFS and BestFS")
    plt.show()
