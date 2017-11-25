'use strict';

angular.module('awd-reflection')
  .config(function($routeProvider) {
    $routeProvider.when('/about', {
      templateUrl: 'app/about/about.html',
      controller: 'AboutCtrl'
    })
  });