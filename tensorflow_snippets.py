#### SOME TENSORFLOW SNIPPETS ####

# METRICS
METRICS = [
      keras.metrics.TruePositives(name='tp'),
      keras.metrics.FalsePositives(name='fp'),
      keras.metrics.TrueNegatives(name='tn'),
      keras.metrics.FalseNegatives(name='fn'), 
      keras.metrics.BinaryAccuracy(name='accuracy'),
      keras.metrics.Precision(name='precision'),
      keras.metrics.Recall(name='recall'),
      keras.metrics.AUC(name='auc'),
]


# CALLBACKS
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('acc')>0.97):
        print("\nReached 97.0% accuracy so cancelling training!")
        self.model.stop_training = True

callbacks = myCallback()# Your Code Here
history = model.fit_generator(train_generator,
                              validation_data=validation_generator,
                              steps_per_epoch=100,
                              epochs=3,
                              validation_steps=50,
                              verbose=2,
                              callbacks=[callbacks],
                             )# Your Code Here (set epochs = 3))