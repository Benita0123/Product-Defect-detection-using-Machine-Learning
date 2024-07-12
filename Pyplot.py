from matplotlib import pyplot as plt


def plot_graph(svc_acc, nb_acc, xgb_acc):

    labels = ['SVC', 'Naive Bayes', 'XGBoost']
    accuracies = [svc_acc, nb_acc, xgb_acc]

    plt.bar(labels, accuracies)
    plt.xlabel('Classifiers')
    plt.ylabel('Accuracy')
    plt.title('Classifier Accuracies')
    plt.ylim(0, 1)
    plt.grid(True)
    plt.show()
    
plot_graph()  