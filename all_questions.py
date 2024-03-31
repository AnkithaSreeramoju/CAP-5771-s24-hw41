# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "A person could be a Home Owner and have a Low Annual Income"    
    answers["(b) explain"] = "There are attribute combinations not explicitly covered by these rules, like a person with High Annual Income and Currently Employed" 
    answers["(c) explain"] = "A person is a Home Owner and Single, the rule applied first could determine the outcome."
    answers["(d) explain"] = "A default class ensures that every instance can be classified even if it does not meet any specific rule's conditions."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "Yes"
    answers["(b)"] = "Yes"
    answers["(c)"] = "No"

    # explain-string: explanation in english prose
    answers["(a) example"] = "An animal cannot simultaneously be an Aerial Creature, Aquatic Creature, warm-blooded, and fit the conditions of R4."
    answers["(b) example"] = "They cover all possible combinations of the given attributes"
    answers["(c) example"] = "Each rule applies to a distinct set of attributes, so the order in which they are applied does not affect the outcome."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = "True"
    answers["(b)"] = "True"
    answers["(c)"] = "False"
    answers["(d)"] = "False"

    # explain_string: explanation in english prose
    answers["(a) explain"] = "The back-propagation algorithm computes the gradient of the loss function with respect to each weight by propagating the error backwards through the network"
    answers["(b) explain"] = "The activations at each layer are computed based on the activations of the previous layer and the current layer’s weights, making it possible to compute activations in a feedforward manner from input to output."
    answers["(c) explain"] = "The vanishing gradient problem refers to the issue where gradients become increasingly smaller as the error is propagated back through the layers, leading to minimal changes in weights and thus slowing down or halting training"
    answers["(d) explain"] = "Gradients of loss with respect to weights at all layers are 0, as small adjustments could still potentially reduce the loss further, especially if regularization is applied."

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "dependent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.25

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int"
    answers["(a) K"] = 1
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "The data points are well separated by class, so a small K value like K = 1 or K = 5 will likely perform well."
    answers["(b) explain"] = "The data points show a significant amount of overlap, and choosing a small K value might lead to misclassification due to noise"

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "P(A=1|+) being 0.6 reflects the likelihood of A occurring in positive conditions, indicating a stronger association with positivity than negativity"
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 1.0 
    answers["(b) P(R|+)"] = 0.2
    answers["(b) P(R|-)"] = 0.0

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # string, '+' or '-'
    answers["(b) class label"]= '+'
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = 'yes'
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = 'No'
    

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "Since this is not the case here (0.2 ≠ 0.24), it indicates that there's some degree of dependency between A and B when the condition is positive"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
