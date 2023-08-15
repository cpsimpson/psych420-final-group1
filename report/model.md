

## Our Model

![High Level Model Overview](images/modeldiagram.png)

We have structured our model to vaguely match the brain structural regions 
with the conceptual functionality we have implemented. We did this, knowing 
that it was a gross over-simplification, as an attempt 
to evaluate the likelihood of the structures of the model being realistic for
the biological system. We feel that the model is not likely to be similarly implemented
in biological brains given the complications in communication at various points.

The core functionality of our model can be found in the model -> brain -> concepts folder. 
Each of the memory types is implemented within dedicated files (and classes). 

### Sensory Memory
The Sensory memory gets primed with a word list at the start of the simulation. 
This loads all "activation" patterns into data structures within SensoryMemory. 
For activation patterns, as mentioned above we have chosen to use the valence, dominance, 
and arousal mean scores mapped to words. As a way to simplify implementation we store this
as both a dictionary mapping and a series of binary trees (within the Factor class). 

### Short Term Memory


### Long Term Memory

### Data Structures

#### Binary Search Tree
Holds a reference to the root node of the tree. All the hard work is done in the Node class.

#### Node
Stored in the binary search trees. Each node contains a value (ex. the valence mean score), a 
list of data (ex. the word), and references to its child nodes - left and right.

#### Factor
Factors each store a binary search tree along with a weight. We create one Factor object
for each of the factors we are using in our representation of words 
(valence, dominance, arousal). 

We had a stretch goal to implement
a learning algorithm for long term memory which could utilize the weight. 
The weight would be used to indicate which of the factors (valence, dominance, arousal) 
would be more influential when looking up values in long term memory. This was not implemented.


## How we could improve our model:

Currently, our memory model examines drift along three affective 
dimensions using a binary search tree to index words by their 
emotional characteristics. As drift occurs the model recalls words 
with similar affective characteristics, but in practice these words 
don’t appear to be logically very similar. While our computational 
model may be “interesting”, in practice it is not a very good 
representation of how human memory works. The process of building 
the model has, however, provided us with insights on how going 
forward we could develop something more complex that better 
approximates biological memory. 

Recent work on human lexical development has found that the affective
dimensions of words are much less useful for predicting the 
development and evolution of language than other types of semantic 
knowledge like logical associations [(Brochhagen et al., 2023)](#brochhagen-et-al-2023). 
In their paper Brochhagen 
used the same lexical database from Warriner that we did to classify 
the affective characteristics of words, but being savvier than us 
they were able to integrate with several other existing databases 
of other kinds of semantic knowledge. Helpfully they’ve even included 
these databases in their open science framework repository, and if we
had more time, we’d make use of these… 

If we were to recreate our model again from scratch, the findings of 
Brochhagen suggest that our focus should really be on other semantic 
dimensions like the associativity of words. Drawing inspiration from 
these other models, instead of using binary search trees for three 
emotional dimensions we could use a multidimensional or kd-tree in 
which all the semantic properties of the words were represented in 
different dimensions [(Ram & Sinha, 2019)](#ram-sinha-2019).

The nearest neighbors search algorithm for kd-trees operates 
similarly to a binary search tree with a few exceptions. The 
dimension you’re searching in rotates at each node. Eventually you 
arrive at a terminal node in multidimensional space that’s near the 
exact values you’re looking for, the search travels back and goes 
through other nodes to ensure that there aren’t any closer nodes, 
the algorithm terminates when the distance of all possible nearest 
neighbors have been examined.

One way to combine properties from the different models we’ve 
examined is here would be using a kd tree with a nearest neighbor’s 
search including all the semantic dimensions available in Brochhagen.
We could use training weights to determine a probabilistic frequency 
with which each dimension should be used at each node to 
“1. Give the right answer most of the time”, or 
“2. Give answers correctly and incorrectly in a manner approximating 
biological memory”.
