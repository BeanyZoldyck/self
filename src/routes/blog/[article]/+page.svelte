<script lang="ts">
	import { page } from '$app/state';
	import Article from './article.svelte';
	let link = $derived(page.params.article || '');
	interface ArticleData {
		link: string;
		title: string;
		header: string;
		created: number;
		edited: number;
	}
	const articles: Array<ArticleData> = [
		{
			link: 'site',
			title: 'personal site',
			header: 'took me long enough',
			created: 1772583770851,
			edited: Date.now()
		}
	];
	function getArticle(ref: string): ArticleData {
		for (const article of articles) {
			if (article.link == ref) return article;
		}
		return {
			link: 'none',
			title: 'Article not found!',
			header: 'just go back to blogs using the button below',
			created: 0,
			edited: Date.now()
		};
	}
</script>

<Article article={getArticle(link)}></Article>
