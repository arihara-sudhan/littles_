<center>
<img src='https://assets.lybrate.com/q_auto:eco,f_auto,w_1200,h_720,c_fill,g_auto/imgs/product/health-wiki/bpages/Benefits-Of-Cherry.jpg' alt='' width='80%'></center>
<h1>INTRODUCTION</h1>
<p>We may want to see whether two images (Faces) are similar or not. Siamese Neural Networks help us here. Using Siamese Network, we can distinguise between faces or any other objects. We know the face-matching-locking system in our phone. What would be the background operation ? (Talkin’ of the training process) You don’t use many photos to perform such training. You use a single or a less number or images for such a training.
We may need a lot of images for such a problem. Isn’t it fascinating when there is no need for that while we use Siamese Network for image verification ? And, it is not even a workload to train a bunch of images since just one person is going to access the phone and training on some images of him is not a sin. But, imagine when an organization uses such an authentication mechanism for it’s employees. The situation becomes a bit worse.
We need n number of images of each employees of the organization to train the network. And another important problem here is the so-called Scalability. If a new employee joins there, we need to retrain the classifier and the situation is HELL. A Simple but efficient solution here is using the SIMILARITY MODEL rather than a CLASSIFIER MODEL. This is where the Siamese Network comes to take a part in our journey.
Let’s make illustrations for a better understanding.<p>
<center>
<img src='https://github.com/arihara-sudhan/SiameseNetwork/blob/b1cde1417970e0da4769bb04249428c4c30b9df1/pics/what.png' alt='' width='90%'>
</center>
<h1>THE IDEA BEHIND</h1>
<p>Now, we just want to know what to do.
Looking at the image above, we can observe that we pass two input images to CNNs of same configurations which have a convolutional layer, Max-Pooling and an FC Layer. Eventually,  feature vectors / embeddings are obtained from these networks. These vectors are to be compared in order to check for similarity. Those feature vectors are passed into a softmax classifier. These two vectors if they are of the same person should be pretty much similar.
On the other hand, if they are of different people, these two vectors should be different. The siamese network uses identical networks.
The difference is found between two vectors using the given formula. It will be small on having similar images and vice versa.</p>
<center>
<img src='https://github.com/arihara-sudhan/SiameseNetwork/blob/b1cde1417970e0da4769bb04249428c4c30b9df1/pics/what2.png' alt='' width='90%'>
</center>
<h1>TRIPLET LOSS</h1>
Computationally speaking, in all sort of neural networks, we define a loss function which must be minimized for a better training. Here, we define the so-called triplet loss. But, why the name “Triplet Loss”? We are about to deal with collection of three data on each epoch. What are those three ? They are Anchor, Positive and a Negative Image. Anchor is the one given to be verified or a ground truth. 
Positive is the one which is similar to the Anchor. Negative is the one which is dissimilar to the Anchor. So, what we can do to go on ? <br>We need the difference between the f(A) and f(P) to be less and that of the f(A) and f(N) to be a bit high. Collectively, d(A,P) should be less than or equal to d(A,N).<br>
||f(A)-f(P)||2 <= ||f(A)-f(N)||2<br>
d(A,P) <= d(A,N)<br>
If we get zero or any other  things, we might end up with equality in both the sides. To avoid this, a margin is used.<br>
d(A,P) <= d(A,N) – α<br>
d(A,P)-d(A,N)+α <= 0<br>
Let D = d(A,P)-d(A,N)+α<br>
Now, we can define the triplet loss as the following :<br>
L(A,P,N) = max(0,D)<br>
For n training samples, we can define the cost function as,<br>
J = Σ(i=0 To m)max(0,D)<br>
Now, let’s learn about contrastive loss which can also be used for this.

<img src='https://github.com/arihara-sudhan/SiameseNetwork/blob/b1cde1417970e0da4769bb04249428c4c30b9df1/pics/arch.png' alt='' width='90%'>
<h1>OUTPUTS</h1>
<img src='https://github.com/arihara-sudhan/SiameseNetwork/blob/b1cde1417970e0da4769bb04249428c4c30b9df1/pics/op1.png' width='90%'>
<img src='https://github.com/arihara-sudhan/SiameseNetwork/blob/b1cde1417970e0da4769bb04249428c4c30b9df1/pics/op2.png' width='90%'>
<img src='https://github.com/arihara-sudhan/SiameseNetwork/blob/b1cde1417970e0da4769bb04249428c4c30b9df1/pics/op3.png'  width='90%'>
