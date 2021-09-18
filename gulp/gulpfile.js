var gulp = require('gulp'),
	autoprefixer = require('gulp-autoprefixer'),
	browserSync = require('browser-sync').create(),
	cleanCSS = require('gulp-clean-css'),
	concat = require('gulp-concat'),
	htmlmin = require('gulp-htmlmin'),
	lineec = require('gulp-line-ending-corrector'),
	reload = browserSync.reload,
	sass = require('gulp-sass'),
	sourcemaps = require('gulp-sourcemaps'),
	uglify = require('gulp-uglify');

/**
*	ROOT URI
*/
var rootSrc = '../',
	rootDest = '../';


var	scssSrc = rootSrc + 'assets/scss/';

// var concatcssSrc = rootSrc + 'assets/css/style.css',
var concatcssSrc = rootSrc + 'assets/css/style.css',
	concatcssDest = rootDest + 'assets/css/';

var jsSrc = rootSrc + 'assets/js/',
	jsconcatSrc = [ 
		jsSrc + 'search_auto.js'
	],
	jsDest = rootDest + 'assets/js/';

// var htmlSrc = rootSrc + '*.html',
// 	htmlDest = rootDest;

/**
*	WATCH FILES
*/

var styleWatch = scssSrc + '**/*.scss';
	// htmlWatch = rootSrc + '**/*.html';

/**
*	SCSS to CSS Conversion
*/

function scssToCss() {
	return gulp.src(
		[ scssSrc + 'style.scss' ])
		.pipe(sourcemaps.init({loadMaps: true}))
		.pipe(sass({outputStyle: 'compact'}).on('error', sass.logError))
		.pipe(autoprefixer('last 2 versions'))
		.pipe(sourcemaps.write())
		.pipe(lineec())
		.pipe(gulp.dest(rootSrc + 'assets/css/'))
		.pipe(browserSync.stream());
}

/**
*	CSS MINIFICATION
*/
function cssMinification() {
	return gulp.src(concatcssSrc)
		.pipe(sourcemaps.init({loadMaps: true, largeFile: true}))
		.pipe(concat('style.min.css'))
		.pipe(cleanCSS())
		.pipe(sourcemaps.write('./maps/'))
		.pipe(lineec())
		.pipe(gulp.dest(concatcssDest))
		.pipe(browserSync.stream());
}

/**
*	JS MINIFICATION
*/
// function jsMinification() {
// 	return gulp.src(jsconcatSrc)
// 		.pipe(concat('build-search.js'))
// 		.pipe(uglify())
// 		.pipe(lineec())
// 		.pipe(gulp.dest(jsDest))
// 		.pipe( browserSync.stream());
// }

/**
*	HTML MINIFICATION
*/
// function htmlMinification() {
// 	return gulp.src(htmlSrc)
// 		.pipe(htmlmin({ collapseWhitespace: true }))
// 		.pipe(gulp.dest(htmlDest));
// }


function watch() {
	// browserSync.init([htmlSrc],{
	// 	server: {
	// 		baseDir: rootDest
	// 	}
	// });
	gulp.watch(styleWatch, gulp.series([scssToCss, cssMinification]));
	// gulp.watch(jsSrc, jsMinification);
	// gulp.watch(htmlSrc, htmlMinification);
	// gulp.watch([htmlWatch]).on('change', browserSync.reload);
}

exports.scssToCss = scssToCss;
exports.cssMinification = cssMinification;
// exports.jsMinification = jsMinification;
// exports.htmlMinification = htmlMinification;
exports.watch = watch;

var build = gulp.parallel(watch);
gulp.task('default', build);