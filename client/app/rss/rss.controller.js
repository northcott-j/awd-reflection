'use strict';

angular.module('awd-reflection')
    .controller('RSSCtrl', function ($scope, $http, $mdDialog) {
        $scope.feeds = [];
        // Gets a new set of rss articles
        $scope.update_rss = function () {
            $http.get("/api/rss/articles")
                .then(function successCallback(response) {
                    $scope.feeds = response.data.slice(0,30);
                })
        };

        $scope.update_rss();
    });