'use strict';

angular.module('awd-reflection', ['ngMaterial', 'ngSanitize', 'ngResource', 'ngRoute', 'ui.bootstrap']).config(function ($mdThemingProvider, $routeProvider, $locationProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('red')
    .accentPalette('blue-grey');
  $routeProvider.otherwise({ redirectTo: '/'
  });
  $locationProvider.html5Mode({
    enabled: true,
    requireBase: false
  });
});