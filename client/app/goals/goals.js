'use strict';

angular.module('awd-reflection')
  .config(function($routeProvider) {
    $routeProvider.when('/', {
      templateUrl: 'app/goals/goals.html',
      controller: 'GoalsCtrl'
    })
  });