'use strict';

angular.module('awd-reflection')
    .controller('GoalsCtrl', function ($scope, $http, $mdDialog) {
        $scope.goals = {};
        $scope.feeds = [];
        $scope.selected_goal = '';
        // Gets the search results for a goal
        $scope.update_feeds = function (goal) {
            $scope.selected_goal = goal;
            $http.get("/api/goals/" + goal)
                .then(function successCallback(response) {
                    $scope.feeds = response.data;
                })
        };

        // Gets possible goals
        $scope.update_goals = function () {
            $http.get("/api/goals")
                .then(function successCallback(response) {
                    $scope.goals = response.data;
                })
        };

        $scope.update_goals();
        $scope.update_feeds(1);
    });