from google.appengine.ext import db
import pickle
import json as simplejson

# Use this property to store python objects.
class ObjectProperty(db.BlobProperty):
	def validate(self, value):
		try:
			result = pickle.dumps(value)
			return value
		except pickle.PicklingError, e:
			return super(ObjectProperty, self).validate(value)

	def get_value_for_datastore(self, model_instance):
		result = super(ObjectProperty, self).get_value_for_datastore(model_instance)
		result = pickle.dumps(result)
		return db.Blob(result)

	def make_value_from_datastore(self, value):
		try:
			value = pickle.loads(str(value))
		except:
			pass
		return super(ObjectProperty, self).make_value_from_datastore(value)

class JsonProperty(db.TextProperty):
	def validate(self, value):
		return value

	def get_value_for_datastore(self, model_instance):
		result = super(JsonProperty, self).get_value_for_datastore(model_instance)
		result = simplejson.dumps(result)
		return db.Text(result)

	def make_value_from_datastore(self, value):
		try:
			value = simplejson.loads(str(value))
		except:
			pass

		return super(JsonProperty, self).make_value_from_datastore(value)