import numpy as np

def loadData(filename):
    # Load data from file into X
    X = []
    count = 0
    
    text_file = open(filename, "r")
    lines = text_file.readlines()
        
    for line in lines:
        X.append([])
        words = line.split(",")
        # Convert values of the first attribute into float
        for word in words:
            if (word=='M'):
                word = 0.333
            if (word=='F'):
                word = 0.666
            if (word=='I'):
                word = 1
            X[count].append(float(word))
        count += 1
    
    return np.asarray(X)

def testNorm(X_norm):
    xMerged = np.copy(X_norm[0])
    # Merge datasets
    for i in range(len(X_norm)-1):
        xMerged = np.concatenate((xMerged,X_norm[i+1]))
    print(np.mean(xMerged,axis=0))
    print(np.sum(xMerged,axis=0))

def dataNorm(X): 
    # Normalise data points for first 8 columns
    for i in range(0, 8): 
        col = X[:,i]
        max_val = col.max() 
        min_val = col.min() 
        X[:,i] = (col-min_val)/(max_val-min_val)
    return X

def splitTT(X_norm, percentTrain): 
    # Split dataset into train and test set based on the percentTrain specified
    # Random shuffling of data before splitting
    np.random.shuffle(X_norm)
    # Get index to split the data and slice the dataset based on the index
    index = round(len(X_norm)*percentTrain)
    X_train, X_test = X_norm[:index,:], X_norm[index:,:]
    X_split = [X_train, X_test]
    return X_split

def splitCV(X_norm, k): 
    # Partition dataset into k-folds based on k (i.e., number of partitions) specified
    # Random shuffling of data before partitioning
    np.random.shuffle(X_norm)
    X_split = []
    # Get the approx. size for each fold
    size = round(len(X_norm)/k)
    # Partition the data based on the size. The remaining data points will be added to the arrays 
    # and attempt to make the size of each array equal. Remaining data points would be left unused. 
    for i in range(k): 
        X_split.append(X_norm[:size,:])
        X_norm = X_norm[size:,:]
    # If there are limited data points, the following code could be use to add the remaining data points 
    # to the partitions: (Extra)
    # if len(X_norm) != 0:
    #     i = 0
    #     for elem in X_norm:
    #         X_split[i] = list(X_split[i])
    #         X_split[i].append(elem)
    #         X_split[i] = np.array(X_split[i])
    #         i+=1
    return X_split

def knn(X_train, X_test, K): 
    predictions = []
    # Generate prediction for X_test
    for row in X_test:
        # Calculate the distance of the data points in X_train for each data point in X_test 
        distances = []
        for row_train in X_train:
            distance = 0
            # Calculated distance based on Euclidean distance
            for i in range(len(row)-1):
                distance += (row[i] - row_train[i])**2
            distance = np.sqrt(distance)
            distances.append((row_train, distance))
        # Sort the distances for the data point of X_test
        distances.sort(key=lambda elem: elem[1])
        # Get the "K" (specified number of neighbours) and predict the class for that data point
        neighbours = []
        for i in range(K):
            neighbours.append(distances[i][0])
        output_vals = [n[-1] for n in neighbours]
        prediction = max(set(output_vals), key=output_vals.count)
        predictions.append(prediction)
    # Calculate the accuracy of the prediction (no. accurate predictions / total predictions)
    accurate_pred = 0 
    pred_count = len(predictions)
    actual = X_test[:,-1]
    for i in range(pred_count):
        if predictions[i] == actual[i]:
            accurate_pred += 1
    accuracy = (accurate_pred/pred_count) * 100.00
    return accuracy

# This is an example the main of KNN with train-and-test + Euclidean
def knnMain(filename,percentTrain,k):
 
    # Data load
    X = loadData(filename)
    # Normalization
    X_norm = dataNorm(X)
    # Data split: train-and-test
    X_split = splitTT(X_norm,percentTrain)
    # KNN: Euclidean
    accuracy = knn(X_split[0],X_split[1],k)
    
    return accuracy

