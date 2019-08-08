from django.core.cache import cache

model_cache_key = 'saved_model.pkl' 
# this key is used to `set` and `get` 
# your trained model from the cache

model = cache.get(model_cache_key) # get model from cache

if model is None:
    # your model isn't in the cache
    # so `set` it
    model = Word2Vec.load(fname) # load model
    cache.set(model_cache_key, model, None) # save in the cache
    # in above line, None is the timeout parameter. It means cache forever

# now predict
prediction = model.predict(...)