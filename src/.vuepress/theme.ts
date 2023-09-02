import { hopeTheme } from 'vuepress-theme-hope';
import navbar from './navbar.js';
import sidebar from './sidebar.js';

export default hopeTheme({
	fullscreen: true,
	hostname: '',

	author: {
		name: 'Sumanth Tatipamula',
		url: 'https://github.com/sumanthtatipamula',
	},

	iconAssets: 'fontawesome-with-brands',

	logo: '/logo.svg',

	repo: 'sumanthtatipamula/competitive_programming',

	docsDir: 'src',

	// navbar
	navbar,

	// sidebar
	sidebar,

	// footer: 'Default footer',

	displayFooter: true,

	encrypt: {
		config: {
			'/demo/encrypt.html': ['1234'],
		},
	},

	metaLocales: {
		editLink: 'Edit this page on GitHub',
	},

	plugins: {
		// You should generate and use your own comment service
		blog: true,
		comment: {
			provider: 'Giscus',
			repo: 'sumanthtatipamula/competitive_programming',
			repoId: 'R_kgDOJqbqmQ',
			category: 'Announcements',
			categoryId: 'DIC_kwDOJqbqmc4CW5vj',
		},

		// All features are enabled for demo, only preserve features you need here
		mdEnhance: {
			align: true,
			attrs: true,
			chart: true,
			codetabs: true,
			demo: true,
			echarts: true,
			figure: true,
			flowchart: true,
			gfm: true,
			imgLazyload: true,
			imgSize: true,
			include: true,
			katex: true,
			mark: true,
			mermaid: true,
			container: true,
			playground: {
				presets: ['ts', 'vue'],
			},
			presentation: {
				plugins: ['highlight', 'math', 'search', 'notes', 'zoom'],
			},
			stylize: [
				{
					matcher: 'Recommended',
					replacer: ({ tag }) => {
						if (tag === 'em')
							return {
								tag: 'Badge',
								attrs: { type: 'tip' },
								content: 'Recommended',
							};
					},
				},
			],
			sub: true,
			sup: true,
			tabs: true,
			vPre: true,
			vuePlayground: true,
		},
		components: {
			// components you want
			components: [
				'AudioPlayer',
				'Badge',
				'BiliBili',
				'CodePen',
				'PDF',
				'Replit',
				'StackBlitz',
				'VideoPlayer',
				'YouTube',
			],
		},
	},
});
