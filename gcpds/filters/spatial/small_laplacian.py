def function_getMontage(montage):
    # Small laplacian
    # Calculates spatial filter matrix for Laplacian derivations.
    ##
    # Returns a spatial filter matrix used to calculate Laplacian derivations as
    # well as indices used to plot in a topographical layout.
    # Assuming that the data vector s is of dimension <samples x channels>, the
    # Laplacian derivation s_lap can then be calculated by s_lap = s * lap.
    # s = signal(channels x time).
    ##
    # Usage:
    ##   [lap, plot_index, n_rows, n_cols] = getMontage(montage)
    ##
    # Input parameters:
    # montage , Matrix containing the topographical layout of the channels. The
    # content of this matrix can be one of the following formats:
    # (1) Channel numbers where channels are located and zeros
    # elsewhere <NxM>
    # (2) Ones where channels are located and zeros elsewhere <NxM>
    # (3) Predefined layout <string>.
    # Examples for each format:
    # (1) montage = [0 3,0 ,
    # 4,1 2 ,
    # ,0 5,0]
    # (2) montage = [0,1,0 ,
    # ,1,1,1 ,
    # ,0,1,0]
    # (3) montage = '16ch'
    ##
    # Output parameters:
    # lap        , Laplacian filter matrix
    # plot_index , Indices for plotting the montage
    # n_rows     , Number of rows of the montage
    # n_cols     , Number of columns of the montage
    ##
    # Copyright by Clemens Brunner, Robert Leeb, Alois Schlögl
    # Version matlab Toolbox Biosig
    # ------------------------------------------------------------------------
    # Version python
    # Frank Y. Zapata C., Luisa F. Velasquez M.
    # Version 2020
    # ------------------------------------------------------------------------
    if isinstance(montage, str):  # Predefined layouts
        if montage == '16ch':
            temp = [[0, 0, 1, 0, 0],
                    [0, 1, 1, 1, 0],
                    [0, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 0],
                    [0, 0, 1, 0, 0]]
        if montage == '22ch':     # Database BCI competition IV dataset 2a.
            temp = [[0, 0, 0, 1, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0]]
        if montage == '24ch':
            temp = [[0, 1, 0, 0, 1, 0, 0, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 0, 0, 1, 0, 0, 1, 0]]
        if montage == '28ch':
            temp = [[0, 0, 0, 1, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [1, 1, 1, 0, 1, 1, 1]]
        if montage == '30ch':
            temp = [[0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        if montage == '58ch':
            temp = [[0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0]],
        if montage == '60ch':
            temp = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0]]
        if montage == '64ch':  # order of channels of database GIGA_MI_ME
            temp = [[0, 0, 0, 0, 1, 33, 34, 0, 0, 0, 0],
                    [0, 0, 0, 2, 3, 37, 36, 35, 0, 0, 0],
                    [0, 7, 6, 5, 4, 38, 39, 40, 41, 42, 0],
                    [0, 8, 9, 10, 11, 47, 46, 45, 44, 43, 0],
                    [0, 15, 14, 13, 12, 48, 49, 50, 51, 52, 0],
                    [0, 16, 17, 18, 19, 32, 56, 55, 54, 53, 0],
                    [24, 23, 22, 21, 20, 31, 57, 58, 59, 60, 61],
                    [0, 0, 0, 25, 26, 30, 63, 62, 0, 0, 0],
                    [0, 0, 0, 0, 27, 29, 64, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0]]
        plot_index = np.where(np.asarray(temp).T == 1)
        n_rows = np.size(np.asarray(temp), 0)
        n_cols = np.size(np.asarray(temp), 1)
    else:  # User-defined layouts in the form of a matrix
        temp = montage
        plot_index = np.where(np.asarray(temp).T == 1)
        n_rows = np.size(np.asarray(temp), 0)
        n_cols = np.size(np.asarray(temp), 1)

    counter = 1
    temp = np.asarray(temp).T
    lap = np.zeros((np.size(temp, 0), np.size(temp, 1)))

    # Used electrode positions instead of ones (format (1))
    positions = []
    if sum(sum(temp)) != (sum(sum(temp > 0))):
        tmp = np.sort(temp[np.where(temp)])
        positions = np.argsort(temp[np.where(temp)])
        temp = temp > 0

    for k1 in range(0, np.size(temp, 1)):
        for k2 in range(0, np.size(temp, 0)):
            if temp[k2, k1] >= 1:
                lap[k2, k1] = counter
                counter = counter + 1

    neighbors = np.empty((counter - 1, 4))
    neighbors[:] = np.nan

    lap_ = np.zeros((lap.size))
    a = 0
    for k1 in range(0, np.size(temp, 1)):
        for k2 in range(0, np.size(temp, 0)):
            lap_[a] = lap[k2][k1]
            a += 1

    neighbors = []
    for col, row in np.ndindex(lap.T.shape):
        if lap[row][col]:
            around = np.array(
                [row + 1, row - 1, col + 1, col - 1], dtype=object)
            pair = np.array([col, col, row, row], dtype=object)

            around[around < 0] = None

            if around[0] >= lap.shape[0]:
                around[0] = None

            if around[2] >= lap.shape[1]:
                around[2] = None

            around[2:], pair[2:] = pair[2:], around[2:].copy()
            indexes = filter(lambda c: None not in c, zip(around, pair))

            neighbors.append(
                ([lap[ind] for ind in indexes if lap[ind]] + [0] * 4)[:4])

    neighbors = np.array(neighbors, dtype=object)
    # neighbors[neighbors==0] = np.nan # colocar los datos en NaN en ceros 0.

    lap = np.eye(neighbors.shape[0], dtype=float)

    for k in range(0, neighbors.shape[0]):
        temp = neighbors[k, neighbors[k, :] != 0].astype(
            int)  # Neighbors of electrode k
        for aa in range(0, len(temp)):
            lap[k, temp[aa] - 1] = -1 / temp.shape[0]

    if not positions:
        lap = lap[positions, positions]

    lap = lap.T
    return lap, plot_index, n_rows, n_cols
