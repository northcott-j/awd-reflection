'use strict';

angular.module('awd-reflection')
  .config(function($routeProvider) {
    $routeProvider.when('/rss', {
      templateUrl: 'app/rss/rss.html',
      controller: 'RSSCtrl'
    })
  });