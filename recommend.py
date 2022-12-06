from sklearn.neural_network import MLPRegressor
import numpy as np

def classify(global_movies, user):
    nn = MLPRegressor(hidden_layer_sizes=(500, 250, 125), activation="logistic", learning_rate="constant", alpha=.2)

    inp = np.array(user.get_inputdata())
    out = np.array(user.get_inputclass())

    nn.fit(inp, out)

    output = []

    for m in global_movies.values():
        m_predict = nn.predict(X=[m.get_data()])
        m.similarity_rating = m_predict
        output.append(m)
    
    return output

