import util
import os
import numpy as np
import pandas as pd


def load_predict_number_dataset(csv_path):
    """Load dataset for view, like, dislike, comment number.

    Args:
         csv_path: Path to CSV file containing dataset.

    Returns:
        view: NumPy array shape (n_examples, 1)
        like: NumPy array shape (n_examples, 1)
        dislike: Numpy array shape(n_examples, 1)
        comment: Numpy array shape(n_examples, 1)
    """
    # Load headers
    with open(csv_path, encoding='gb18030', errors='ignore', newline='') as csv_fh:
        headers = csv_fh    .readline().strip().split(',')
    # Load features and labels
    view_cols = [i for i in range(len(headers)) if headers[i] == 'views']
    likes_cols = [i for i in range(len(headers)) if headers[i] == 'likes']
    dislikes_cols = [i for i in range(len(headers)) if headers[i] == 'dislikes']
    comment_cols = [i for i in range(len(headers)) if headers[i] == 'comment_count']
    views = np.array(pd.read_csv(csv_path, usecols = view_cols)).ravel()
    likes = np.array(pd.read_csv(csv_path, usecols = likes_cols)).ravel()
    dislikes = np.array(pd.read_csv(csv_path, usecols = dislikes_cols)).ravel()
    comment_count = np.array(pd.read_csv(csv_path, usecols = comment_cols)).ravel()

    return views, likes, dislikes, comment_count

def load_number_dataset(csv_path, header):
    """Load dataset for view, like, dislike, comment number.

    Args:
         csv_path: Path to CSV file containing dataset.
         header: input the header of column (type: string)

    Returns:
        view: NumPy array shape (n_examples, 1)
        like: NumPy array shape (n_examples, 1)
        dislike: Numpy array shape(n_examples, 1)
        comment: Numpy array shape(n_examples, 1)
    """
    # Load headers
    with open(csv_path, encoding='gb18030', errors='ignore', newline='') as csv_fh:
        headers = csv_fh    .readline().strip().split(',')
    # Load features and labels
    cols = [i for i in range(len(headers)) if headers[i] == header]
    data = np.array(pd.read_csv(csv_path, usecols = cols)).ravel()


    return data