<script lang="ts">
	import { page } from '$app/state';
	import Article from './article.svelte';
	let link = $derived(page.params.article || '');
	interface ArticleData {
		link: string;
		title: string;
		header: string;
	}
	const articles: Array<ArticleData> = [
		{
			link: 'site',
			title: 'personal site',
			header: 'took me long enough'
		}
	];
	function getArticle(ref: string): ArticleData {
		for (const article of articles) {
			if (article.link == ref) return article;
		}
		return {
			link: 'none',
			title: 'Article not found!',
			header: 'just go back to blogs using the button below'
		};
	}
</script>

<Article article={getArticle(link)}></Article>
