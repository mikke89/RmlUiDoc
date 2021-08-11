---
layout: page
title: Search
include_in_search_results: false
---

<script src="{{ "/assets/scripts/lunr.js" | relative_url }}"></script>

<form style="text-align: center" id="form-search" class="form-search" action="" method="get">
  <input type="search" class="input-medium search-query" id="search-box" placeholder="Search..." name="q">
  <input type="submit" class="btn" value="Search">
</form>

---

<div id="search-results"></div>


<script>
function getQueryParam(variable) {
	var query = window.location.search.substring(1);
	var vars = query.split('&');

	for (var i = 0; i < vars.length; i++) {
		var pair = vars[i].split('=');

		if (pair[0] === variable) {
			return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
		}
	}
	return '';
}
function setQueryParam(key, value, replace_state) {
	if (typeof(URLSearchParams) != "undefined" && history.pushState) {
		var params = new URLSearchParams(window.location.search);
		params.set(key, value);
		var newUrl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?' + params.toString();
		var state_obj = {
			path: newUrl
		};
		if (replace_state)
			window.history.replaceState(state_obj, '', newUrl);
		else
			window.history.pushState(state_obj, '', newUrl);
	}
}

var pages = [
{% for page in site.pages %}
	{% if page.include_in_search_results and page.title %}
		{% capture parent_url %}/pages/{{ page.parent }}{% endcapture %}
		{% capture grandparent_url %}/pages/{{ page.grandparent }}{% endcapture %}
		{% assign parent_title = "" %}
		{% assign grandparent_title = "" %}
		{% for it_page in site.pages %}
			{% if it_page.url == parent_url %}
				{% assign parent_title = it_page.short_title | default: it_page.title %}
			{% endif %}
			{% if it_page.url == grandparent_url %}
				{% assign grandparent_title = it_page.short_title | default: it_page.title %}
			{% endif %}
		{% endfor %}
		{% if grandparent_title != "" %}
			{% capture parent_title %}{{ grandparent_title }} / {{ parent_title }}{% endcapture %}
		{% endif %}
		
		{
		"title": "{{ page.title }}",
		"property": "",
		"element": "",
		"url": "{{ page.url }}",
		"parent_title": "{{ parent_title }}",
		"content": "{{ page.content | markdownify | strip_html | replace: '"', " " | replace: "\", " " | normalize_whitespace }}"
		},
	{% endif %}
{% endfor %}
{% include elements_and_properties.index %}
];

var idx = lunr(function () {
	this.ref('id')
	this.field('title', {
		boost: 10
	})
	this.field('property', {
		boost: 100
	})
	this.field('element', {
		boost: 100
	})
	this.field('content')
	this.metadataWhitelist = ['position']

	pages.forEach(function (doc, index) {
		doc['id'] = index;
		this.add(doc)
	}, this)
});

function displaySearchResults(has_search_text, results, pages) {
	function mergePositions(positions, new_positions) {
		positions = positions.concat(new_positions);
		positions.sort(function (a, b) {
			return a[0] - b[0];
		});

		for (var i = 0; i < positions.length - 1; i++) {
			var pos = positions[i];
			var pos_next = positions[i + 1];

			if (pos[0] + pos[1] > pos_next[0]) {
				pos[1] = Math.max(pos[1], pos_next[0] + pos_next[1] - pos[0]);

				delete positions[i + 1];
				i--;
			}
		}

		return positions;
	}

	var el_search_results = document.getElementById('search-results');

	if (results.length && has_search_text) {
		var results_string = '';
		const max_results = 15;
		const max_elements_and_properties = 8;
		var num_elements_and_properties = 0;

		for (var i = 0; i < results.length && i < max_results + num_elements_and_properties; i++) {
			var item = pages[results[i].ref];

			var title = item.title;
			const summary_length = 200;
			var content = item.content;
			var property = item.property;
			var element = item.element;
			var url = '{{ "" | relative_url }}' + item.url;

			if (element.length || property.length) {
				num_elements_and_properties++;
				if (num_elements_and_properties > max_elements_and_properties)
					continue;
			}
			
			var content_positions = [];
			var title_positions = [];
			var property_positions = [];
			var element_positions = [];

			for (var query in results[i].matchData.metadata) {
				var match_objects = results[i].matchData.metadata[query];
				if ('content' in match_objects) {
					content_positions = mergePositions(content_positions, match_objects['content'].position);
				}
				if ('title' in match_objects) {
					title_positions = mergePositions(title_positions, match_objects['title'].position);
				}
				if ('property' in match_objects) {
					property_positions = mergePositions(property_positions, match_objects['property'].position);
				}
				if ('element' in match_objects) {
					element_positions = mergePositions(element_positions, match_objects['element'].position);
				}
			}

			function highlightMatches(content, positions, skip_after_index) {
				var cursor = 0;
				var new_content = "";
				for (var j = 0; j < positions.length; j++) {
					var pos = positions[j];
					if (skip_after_index && pos[0] > skip_after_index)
						break;
					new_content += content.slice(cursor, pos[0]) + '<strong>' + content.slice(pos[0], pos[0] + pos[1]) + '</strong>';
					cursor = pos[0] + pos[1];
				};

				new_content += content.slice(cursor);
				return new_content;
			}

			if (content_positions.length) {
				var first_match = content_positions[0][0];
				var summary_begin = Math.max(0, content.lastIndexOf(' ', Math.max(0, first_match - 60)));
				var summary_end = first_match + summary_length;

				var new_content = highlightMatches(content, content_positions, summary_end);

				var i_strong = new_content.indexOf('</strong>', summary_end);
				summary_end = Math.max(new_content.indexOf(' ', summary_end), i_strong < 0 ? -1 : i_strong + '</strong>'.length);
				summary_end = summary_end < 0 ? new_content.length : summary_end;

				content = new_content.slice(summary_begin, summary_end);

			} else {
				content = content.substring(0, Math.max(summary_length, content.indexOf(' ', summary_length)));
			}

			if (title_positions.length) {
				title = highlightMatches(title, title_positions, false);
			}
			if (property_positions.length) {
				property = highlightMatches(property, property_positions, false);
			}
			if (element_positions.length) {
				element = highlightMatches(element, element_positions, false);
			}
			
			if (property.length) {
				results_string += '<h4 title="RCSS property"><span class="fas">&#xf121;</span><a href="' + url + '">‘' + property + '’ property</a></h4>';
			} else if (element.length) {
				results_string += '<h4 title="RML element"><span class="fas">&#xf84c;</span><a href="' + url + '">&lt;' + element + '&gt; element</a></h4>';
			} else {
				results_string += '<h4><a href="' + url + '">' + title + (item.parent_title ? ' (' + item.parent_title + ')' : '') + '</a></h4>';
				results_string += '<p>' + content + '...</p>';
			}
		}

		results_string += '<p style="text-align: right"><em>Showing ' + Math.min(results.length, max_results + num_elements_and_properties) + ' of ' + results.length + ' ' + (results.length == 1 ? 'result' : 'results') + '.</em></p>';

		el_search_results.innerHTML = results_string;
	} else if (has_search_text) {
		el_search_results.innerHTML = '<p><em>No results found.</em></p>';
	} else {
		el_search_results.innerHTML = '<p><em>Please enter a search term above.</em></p>';
	}
}

var el_search_box = document.getElementById('search-box');

function doSearch() {
	var search_term = el_search_box.value;
	var results = idx.search(search_term);
	displaySearchResults(Boolean(search_term), results, pages);
}

document.getElementById('form-search').addEventListener("submit", function (e) {
	e.preventDefault();
	doSearch();
	setQueryParam('q', el_search_box.value, false);
});

document.getElementById('search-box').addEventListener("input", function (e) {
	doSearch();
	setQueryParam('q', el_search_box.value, true)
});

window.addEventListener("popstate", function (e) {
	var search_term = getQueryParam('q');
	el_search_box.value = search_term;
	doSearch();
});

el_search_box.value = getQueryParam('q');
doSearch();
</script>
