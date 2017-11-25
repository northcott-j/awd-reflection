'use strict';

angular.module('awd-reflection')
  .directive('navbar', [function () {
    'use strict';
    return {
        templateUrl: 'components/header/header.html',
        restrict: 'E',
        scope: {
            currentPage: '=page'
        },
        controller: 'NavHeaderController',
        controllerAs: 'navHeader'
    }
  }]);