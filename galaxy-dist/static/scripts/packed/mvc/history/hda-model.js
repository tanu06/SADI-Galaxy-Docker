define(["mvc/dataset/dataset-model","mvc/history/history-content-model","mvc/base-mvc","utils/localization"],function(e,g,b,c){var f=e.DatasetAssociation,d=g.HistoryContentMixin;var a=f.extend(b.mixin(d,{constructor:function(i,h){d.constructor.call(this,i,h)},defaults:_.extend({},f.prototype.defaults,d.defaults,{model_class:"HistoryDatasetAssociation"}),initialize:function(h,i){f.prototype.initialize.call(this,h,i);d.initialize.call(this,h,i)},toString:function(){var h=this.get("id")||"";if(this.get("name")){h=this.get("hid")+' :"'+this.get("name")+'",'+h}return"HDA("+h+")"}}));return{HistoryDatasetAssociation:a}});