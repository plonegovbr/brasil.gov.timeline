import TimeLineTile from './js/tiles/timeline.js';

// https://hacks.mozilla.org/2015/04/es6-in-depth-iterators-and-the-for-of-loop/
jQuery.prototype[Symbol.iterator] = Array.prototype[Symbol.iterator];


$(() => {
  for (let timeline of $('.brasil-gov-timeline-tile')) {
    new TimeLineTile(timeline);
  }
});



export default {
  TimeLineTile,
}
