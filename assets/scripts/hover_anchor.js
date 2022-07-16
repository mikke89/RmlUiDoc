let linkifyAnchors = function (tag, containingElement) {
	let headers = containingElement.getElementsByTagName(tag);
	
	for (let h = 0; h < headers.length; h++) {
		let header = headers[h];
		if (typeof header.id !== "undefined" && header.id !== "") {
			let anchor = document.createElement("a");
			anchor.className = "header-link";
			anchor.href      = "#" + header.id;
			header.appendChild(anchor);
		}
	}
};

document.onreadystatechange = function () {
	if (this.readyState === "complete") {
		let containingElement = document.getElementById("anchor-container");
		if (!containingElement)
			return;
		
		let anchorTags = ["h3","h4"];
		for (let i = 0; i < anchorTags.length; i++) {
			linkifyAnchors(anchorTags[i], containingElement);
		}
	}
};
