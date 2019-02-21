# Introduction to Word Embeddings

![img](https://cdn-images-1.medium.com/max/1600/0*IiCawLxDf1qyo7Tq.png)

### What is a word embedding?

A very basic definition of a word embedding is a real number, vector representation of a word. Typically, these days, words with similar meaning will have vector representations that are close together in the embedding space (though this hasn’t always been the case).

When constructing a word embedding space, typically the goal is to capture some sort of relationship in that space, be it meaning, morphology, context, or some other kind of relationship.

By encoding word embeddings in a densely populated space, we can represent words numerically in a way that captures them in vectors that have tens or hundreds of dimensions instead of millions (like one-hot encoded vectors).

A lot of word embeddings are created based on the notion introduced by [Zellig Harris’ “distributional hypothesis”](https://aclweb.org/aclwiki/Distributional_Hypothesis) which boils down to a simple idea that words that are used close to one another typically have the same meaning.

The beauty is that different word embeddings are created either in different ways or using different text corpora to map this distributional relationship, so the end result are word embeddings that help us on different down-stream tasks in the world of NLP.

### Why do we use word embeddings?

Words aren’t things that computers naturally understand. By encoding them in a numeric form, we can apply mathematical rules and do matrix operations to them. This makes them amazing in the world of machine learning, especially.

Take deep learning for example. By encoding words in a numerical form, we can take many deep learning architectures and apply them to words. Convolutional neural networks have been applied to NLP tasks using word embeddings and have set the state-of-the-art performance for many tasks.

Even better, what we have found is that we can actually pre-train word embeddings that are applicable to many tasks. That’s the focus of many of the types we will address in this article. So one doesn’t have to learn a new set of embeddings per task, per corpora. Instead, we can learn general representation which can then be used across tasks.

### Specific examples of word embeddings

So now with that brief introduction out of the way, let’s take a brief look into some of the different ways we can numerically represent words (and at a later time, I’ll put together a more complex analysis of each and how to actually use them in a down-stream task).

### One-Hot Encoding (Count Vectorizing)

One of the most basic ways we can numerically represent words is through the one-hot encoding method (also sometimes called [count vectorizing](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)).

The idea is super simple. Create a vector that has as many dimensions as your corpora has unique words. Each unique word has a unique dimension and will be represented by a 1 in that dimension with 0s everywhere else.

The result of this? Really huge and sparse vectors that capture absolutely no relational information. It could be useful if you have no other option. But we do have other options, if we need that semantic relationship information.

![One-Hot Encoding](https://cdn-images-1.medium.com/max/1600/1*YEJf9BQQh0ma1ECs6x_7yQ.png)

I also have an post now about how to use count vectorization on real text data! If you’re interested, check it out here: [Natural Language Processing: Count Vectorization with scikit-learn](http://hunterheidenreich.com/blog/nlp-count-vectorization/)

### TF-IDF Transform

[TF-IDF vectors](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) are related to one-hot encoded vectors. However, instead of just featuring a count, they feature numerical representations where words aren’t just there or not there. Instead, words are represented by their term frequency multiplied by their inverse document frequency.

In simpler terms, words that occur a lot but everywhere should be given very little weighting or significance. We can think of this as words like `the` or `and`in the English language. They don’t provide a large amount of value.

However, if a word appears very little or appears frequently, but only in one or two places, then these are probably more important words and should be weighted as such.

Again, this suffers from the downside of very high dimensional representations that don’t capture semantic relatedness.



![img](https://cdn-images-1.medium.com/max/1600/0*TxLEjt20ywuaLUUZ.JPG)

### Co-Occurrence Matrix

A co-occurrence matrix is exactly what it sounds like: a giant matrix that is as long and as wide as the vocabulary size. If words occur together, they are marked with a positive entry. Otherwise, they have a 0. It boils down to a numeric representation that simple asks the question of “Do words occur together? If yes, then count this.”

And what can we already see becoming a big problem? Super large representation! If we thought that one-hot encoding was high dimensional, then co-occurrence is high dimensional squared. That’s a lot of data to store in memory.



![img](https://cdn-images-1.medium.com/max/1600/0*dUiOP5hXMRVR0FaD.png)

### [Neural Probabilistic Model](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)

Now, we can start to get into some neural networks. A neural probabilistic model learns an embedding by achieving some task like modeling or classification and is what the rest of these embeddings are more or less based on.

Typically, you clean your text and create one-hot encoded vectors. Then, you define your representation size (300 dimensional might be good). From there, we initialize the embedding to random values. It’s the entry point into the network, and back-propagation is utilized to modify the embedding based on whatever goal task we have.

This typically takes a lot of data and can be very slow. The trade-off here is that it learns an embedding that is good for the text data that the network was trained on as well as the NLP task that was jointly learned during training.

![Neural Probabilistic Model](https://cdn-images-1.medium.com/max/1600/1*EqKiy4-6tuLSoPP_kub33Q.png)

### word2vec

[Word2Vec](https://code.google.com/archive/p/word2vec/) is a better successor to the neural probabilistic model. We still use a statistical computation method to learn from a text corpus, however, its method of training is more efficient than just simple embedding training. It is more or less the standard method for training embeddings the days.

It is also the first method that demonstrated classic vector arithmetic to create analogies:



![img](https://cdn-images-1.medium.com/max/1600/0*4ctH2ps5Y-ZIYW1g.png)

There are two major learning approaches.

### Continuous Bag-of-Words (CBOW)

This method learns an embedding by predicting the current words based on the context. The context is determined by the surrounding words.

### Continuous Skip-Gram

This method learns an embedding by predicting the surrounding words given the context. The context is the current word.

Both of these learning methods use local word usage context (with a defined window of neighboring words). The larger the window is, the more topical similarities that are learned by the embedding. Forcing a smaller window results in more semantic, syntactic, and functional similarities to be learned.

So, what are the benefits? Well, high quality embeddings can be learned pretty efficiently, especially when comparing against neural probabilistic models. That means low space and low time complexity to generate a rich representation. More than that, the larger the dimensionality, the more features we can have in our representation. But still, we can keep the dimensionality a lot lower than some other methods. It also allows us to efficiently generate something like a billion word corpora, but encompass a bunch of generalities and keep the dimensionality small.

### GloVe

[GloVe](https://nlp.stanford.edu/projects/glove/) is an extension of word2vec, and a much better one at that. There are a set of classical vector models used for natural language processing that are good at capturing global statistics of a corpus, like LSA (matrix factorization). They’re very good at global information, but they don’t capture meanings so well and definitely don’t have the cool analogy features built in.

GloVe’s contribution was the addition of global statistics in the language modeling task to generate the embedding. There is no window feature for local context. Instead, there is a word-context/word co-occurrence matrix that learns statistics across the entire corpora.

The result? A much better embedding being learned than simple word2vec.



![img](https://cdn-images-1.medium.com/max/1600/0*EpDIQufk90qSY7a_.png)

### FastText

Now, with [FastText](https://github.com/facebookresearch/fastText) we enter into the world of really cool recent word embeddings. What FastText did was decide to incorporate sub-word information. It did so by splitting all words into a bag of n-gram characters (typically of size 3–6). It would add these sub-words together to create a whole word as a final feature. The thing that makes this really powerful is it allows FastText to naturally support out-of-vocabulary words!

This is huge because in other approaches, if the system encounters a word that it doesn’t recognize, it just has to set it to the unknown word. With FastText, we can give meaning to words like circumnavigate if we only know the word navigate, because our semantic knowledge of the word navigate can help use at least provide a bit more semantic information to circumnavigate, even if it is not a word our system learned during training.

Beyond that, FastText uses the skip-gram objective with negative sampling. All sub-words are positive examples, and then random samples from a dictionary of words in the corpora are used as negative examples. These are the major things that FastText included in its training.

Another really cool thing is that Facebook, in developing FastText, has published pre-trained FastText vectors in 294 different languages. This is something extremely awesome, in my opinion, because it allows developers to jump into making projects in languages that typically don’t have pre-trained word vectors at a very low cost (since training their own word embeddings takes a lot of computational resources).

If you want to see all the languages that FastText supports, check it out [here](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md).



![img](https://cdn-images-1.medium.com/max/1600/0*pFLiZvEFjMv9Dz_o)

### Poincare Embeddings (Hierarchal Representations)

[Poincare embeddings](https://radimrehurek.com/gensim/models/poincare.html) are really different and really interesting, and if you are feeling ambitious, you should definitely give [the paper](https://arxiv.org/pdf/1705.08039.pdf) a read. They decide to use hyperbolic geometry to capture hierarchal properties of words. By placing their embedding into a hyperbolic space, they can use properties of hyperbolic space to use distance to encode similarity and the norm of vectors to encode hierarchal relationships.

The end result is that less dimensions are needed in order to encode hierarchal information, which they demonstrate by recreating WordNet with very low dimensionality, especially when compared to other word embedding schemes. They highlight how this approach is super useful for data that is extremely hierarchal like WordNet or like a computer network. It will be interesting to see what kind of research, if any, comes out of this stream.



![img](https://cdn-images-1.medium.com/max/1600/0*3qrc9JFYIVLkICeZ)

### ELMo

[ELMo](https://allennlp.org/elmo) is a personal favorite of mine. They are state-of-the-art contextual word vectors. The representations are generated from a function of the entire sentence to create word-level representations. The embeddings are generated at a character-level, so they can capitalize on sub-word units like FastText and do not suffer from the issue of out-of-vocabulary words.

ELMo is trained as a bi-directional, two layer LSTM language model. A really interesting side-effect is that its final output is actually a combination of its inner layer outputs. What has been found is that the lowest layer is good for things like POS tagging and other more syntactic and functional tasks, whereas the higher layer is good for things like word-sense disambiguation and other higher-level, more abstract tasks. When we combine these layers, we find that we actually get incredibly high performance on downstream tasks out of the box.

The only questions on my mind? How can we reduce the dimensionality and extend to training on less popular languages like we have for FastText.

![ELMo Vectors](https://cdn-images-1.medium.com/max/1600/1*gpBBcQbdtIceERjJ784j1A.png)

### Probabilistic FastText

[Probabilistic FastText](https://github.com/benathi/multisense-prob-fasttext) is a [recent paper](https://arxiv.org/pdf/1806.02901.pdf) that came out that tried to better handle the issue of words that have different meanings, but are spelled the same. Take for example the word rock. It can mean:

- Rock music
- A stone
- The action of moving back and forth

How do we know what we are talking about when we encounter this word? Typically, we don’t. When learning an embedding, we just smush all the meanings together and hope for the best. That’s why things like ELMo, which use the entire sentence as a context, tend to perform better when needing to distinguish the different meanings.

That’s also what Probabilistic FastText does really well. Instead of representing words as vectors, words are represented as Gaussian mixture models. Now, I still don’t understand the math really well, but a lot of the training schema is still similar to FastText, just instead of learning a vector, we learn something probabilistic.

I’m very curious to see if this stream yields future research as I think moving away from vectors is a very curious way to go.



![img](https://cdn-images-1.medium.com/max/1600/0*bXz8Iqkfa-Rd-FSg.png)

### Wrapping Up

If you enjoyed reading this article, drop me a comment or maybe donate to my [GoFundMe](https://www.gofundme.com/hunter-heidenreich-research-fund) to help me continue with my ML research!

And stay tuned for more word embedding content coming soon!