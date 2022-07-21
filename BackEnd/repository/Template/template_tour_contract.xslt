<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:ex="http://exslt.org/dates-and-times" xmlns:inv="http://laphoadon.gdt.gov.vn/2014/09/invoicexml/v1" xmlns:sign="http://www.w3.org/2000/09/xmldsig#" xmlns:ddwrt="http://schemas.microsoft.com/WebParts/v2/DataView/runtime" extension-element-prefixes="ex">
	<xsl:decimal-format name="decimalFormat" decimal-separator="," grouping-separator="." zero-digit="0" digit="#" pattern-separator=";"></xsl:decimal-format>
	<xsl:decimal-format name="number" decimal-separator="," grouping-separator="." />
	<xsl:output method="html" />
	<xsl:template match="Contract">
		<xsl:text disable-output-escaping="yes">&lt;</xsl:text>!DOCTYPE html<xsl:text disable-output-escaping="yes">&gt;</xsl:text><html>
			<head>
				<title>Hợp đồng du lịch</title>
				<style>
					body {
					padding: 0;
					margin: 0;
					}

					div {
					box-sizing: content-box;
					line-height: 20px;
					}

					.d-flex{
					display: -webkit-box; /* wkhtmltopdf uses this one */
					display: flex;
					}
					
					.flex-column{
					flex-direction: column;
					-webkit-flex-direction: column;
					}
					
					.container {
					width: 865px;
					overflow: visible;
					position: relative;
					}

					.ruler-template{
					padding-top: 40px;
					margin-left: 45px;
					margin-right: 45px;
					box-sizing: border-box;
					}

					.content-detail{
					min-height: 1068px;
					max-width: 775px;
					}

					.font-bold{
					font-weight: bold;
					}

					.font-italic{
					font-style: italic;
					}

					.text-left {
					text-align: left;
					}

					.text-center {
					text-align: center;
					}

					.text-right {
					text-align: right;
					}

					.float-left{
					float: left;
					}

					.float-right{
					float: right;
					}

					.clear{
					clear:both;
					}

					.display-table-cell{
					display: table-cell;
					}

					.white-space-nowrap{
					white-space: nowrap;
					}

					.style-title {
					font-weight: bold;
					text-transform: uppercase;
					font-size: 20px;
					}

					.style-title .edit-label-en {
					font-weight: bold;
					text-transform: uppercase;
					font-size: 18px;
					}

					.width-full{
					width:100%;
					}

					.width-half{
					width:50%;
					}

					.width-third{
					width:30%;
					}

					.width-quarter{
					width:25%;
					}

					.display-none{
					display: none;
					}

					.seller-infor .edit-value, .buyer-infor .edit-value, .other-invoice .edit-value, .curency-block .edit-value,
					.seller-infor .edit-label-en, .buyer-infor .edit-label-en, .other-invoice .edit-label-en, .curency-block .edit-label-en, .table-footer .edit-label-en {
					padding-left: 4px;
					}

					.seller-infor, .buyer-infor {
					text-align: left;
					}

					.padding-none{
					padding: 0 !important;
					}


					.logo-template{
					z-index: -1;
					}
					.logo-template-content{
					position: relative;
					background-position-x: 0px;
					background-position-y: center;
					background-size:100% 100%;
					background-image: url('data:image/jpg;base64,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');
					height: 80px;
					width: 80px;
					top: 0px;
					left: 0px;
					}

					.information-company{
					width: 100%;
					}

					.header-invoice{
					padding-top: 2px;
					padding-top:20px;
					}

					.other-invoice{
					}
					.type-invoice{
					}

					.buyer-infor{
					width:86%;
					}

					.style-number-value {
					padding-right: 4px;
					}
					
					.title-invoice{
					text-align: center;
					font-size: 30px;
					}

					.padding-left-4{
					padding-left: 4px;
					}

					.number {
					text-align: right;
					}

					.content-sign{
					width: 250px;
					padding:5px;
					color: #db0000;
					position: relative;
					background-color: #e3f2e4;
					border: 1px solid #7cc576;
					margin-top: 20px;
					margin-left: auto;
					margin-right: auto;
					}

					.vertical-align-top{
					vertical-align: top;
					}

					.background-sign{
					background: url('data:image/png;base64,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') no-repeat center center;
					}

					.block-tax-code{
					width: 20px;border:
					1px solid #b7b7b7;
					line-height: 20px;
					padding-top: 2px;
					}

					.sign-xml-block {
					margin-top: 8px;
					}

					.invoice-information {
					width: 100%;
					border-collapse: collapse;
					}

					.element-help-center {
					width: 145px;
					}

					.inv-series-no {
					width: 145px;
					}

					.inv-series-no-en {
					width: 190px;
					}

					.vertical-align-top {
					vertical-align: top;
					}

					.edit-label-en {
					font-style: italic;
					font-size: 13px;
					}

					.sign-content-convert {
					margin-top: 90px;
					}

					.padding-left-2 {
					padding-left: 2px;
					}

					.width-converter {
					width: 550px;
					}

					.display-cannot-show {
					display: none;
					}

					.padding-left-16 {
					padding-left: 16px;
					}
					
					.edit-value{
					padding-left: 4px;
					}

					.seller-infor .edit-label-en, .seller-infor .edit-label, .buyer-infor .edit-label-en, .buyer-infor .edit-label {
					white-space: nowrap;
					}

					.other-table-container {
					vertical-align: top;
					}

					.text-en-fake {
					white-space: nowrap;
					font-style: italic;
					font-size: 13px;
					}

					#signXml .white-space-nowrap {
					white-space: nowrap;
					}

					.template-table{
					<!--##BG_TABLE##-->background: url('');<!--##BG_TABLE##-->
					background-repeat:no-repeat;
					background-position: center;
					position:absolute;
					z-index: 100;
					width:100%;
					height:100%
					}

					.p-relative {
					position: relative;
					}

					.esign-value-company {word-break: break-word;}

					td[data-field="ItemName"] .edit-value {white-space: pre-line;}

					.flex {
					display: flex;
					}

					.justify-center {
					justify-content: center
					}

					.break-all {
					word-break: break-all;
					}

					.width-third {
					width: 33.33%;
					}

					.exchange-rate {
					<!--##ExchangeRate##--><!--##ExchangeRate##-->
					}
					.exchange-rate-table {
					<!--##ExchangeRateTable##--><!--##ExchangeRateTable##-->
					}
					
					.sign-content{
					height:200px;
					background-repeat: no-repeat;
					background-size: cover;
					}
					
					.buyer-sign-content{
					<!--##CONTENT_BUYER_SIGN##-->background-image: url()<!--##CONTENT_BUYER_SIGN##-->
					}
					
					.seller-sign-content{
					<!--##CONTENT_SELLER_SIGN##-->background-image: url()<!--##CONTENT_SELLER_SIGN##-->
					}
					
					@media print {
						.content-block{
						page-break-before: auto;
						}
					}
					<!--##CUSTOM_STYLE##--><!--##CUSTOM_STYLE##-->
				</style>
			</head>
			<body>
				<div id="TemplateType" style="display:none">A4</div>
				<div class="container">
					<div class="auContent ruler-template">
						<div class="content-detail" style="">
							<div class="header-block">
								<div class="seller-infor d-flex">
									<div class="logo-template-content" style="margin-right:25px"></div>
									<div class="flex-column">
										<div class="edit-item disable-hiden width-full type-2" data-field="SellerName" style="">
											<div class="edit-label display-table-cell white-space-nowrap display-none" style="min-width: 0px;">Đơn vị bán hàng</div>
											<div class="two-dot display-table-cell white-space-nowrap display-none" style="">:</div>
											<div class="edit-value display-table-cell font-bold style-title padding-none none-edit header-title" style="margin-left: 0px;">
												<xsl:value-of select="ProviderName" />
											</div>
										</div>
										<div class="edit-item width-full type-1" data-field="SellerAddress" style="">
											<div class="edit-label display-table-cell white-space-nowrap" style="">Địa chỉ</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px; font-size: 14px;">
												<xsl:value-of select="ProviderAddress" />
											</div>
										</div>
										<div class="edit-item width-full type-1" data-field="SellerPhone" style="">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Điện thoại</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="min-width: unset;">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="ProviderPhone" />
											</div>
										</div>
										<div class="edit-item width-full type-1" data-field="SellerEmail" style="">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Email</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="min-width: unset;">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="ProviderEmail" />
											</div>
										</div>
									</div>
								</div>
								<div class="header-invoice invoice-second highlight-block flex-column">
									<div class="width-full d-flex">
										<div class="flex-column width-half">
											<div class="edit-item disable-hiden width-full type-2" data-field="SellerName" style="padding-bottom:10px">
												<div class="edit-label display-table-cell white-space-nowrap display-none" style="min-width: 0px;">Đơn vị bán hàng</div>
												<div class="two-dot display-table-cell white-space-nowrap display-none" style="">:</div>
												<div class="edit-value display-table-cell font-bold style-title padding-none none-edit header-title" style="margin-left: 0px;">
													<xsl:value-of select="ProviderName" />
												</div>
											</div>
											<div class="edit-item disable-hiden width-full type-2" data-field="ContractNo" style="">
												<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Hợp đồng số</div>
												<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
												<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
													<xsl:value-of select="ContractCode" />
												</div>
											</div>
										</div>
										<div class="flex-column width-half">
											<div class="font-bold text-center">CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM</div>
											<div class="font-bold text-center" style="padding-bottom:5px;">Độc lập - Tự do - Hạnh phúc</div>
											<div class="disable-hiden font-italic text-center" data-field="DateInvoice" style="padding-top:5px">
												<div class="edit-value none-edit font-italic" style="">
													<xsl:variable name="issuedDate" select="CreatedTime" />
													<xsl:choose>
														<xsl:when test="$issuedDate != ''">
															<span>Ngày</span>
															<span class="padding-left-4">
																<xsl:value-of select="substring($issuedDate, 9, 2)" />
															</span>
															<span class="padding-left-4">tháng</span>
															<span class="padding-left-4">
																<xsl:value-of select="substring($issuedDate, 6, 2)" />
															</span>
															<span class="padding-left-4">năm</span>
															<span class="padding-left-4">
																<xsl:value-of select="substring($issuedDate, 1, 4)" />
															</span>
														</xsl:when>
														<xsl:otherwise>
															<span class="date-text">Ngày</span>
															<span class="month-text padding-left-16 ">tháng</span>
															<span class="year-text padding-left-16 ">năm</span>
														</xsl:otherwise>
													</xsl:choose>
												</div>
											</div>
										</div>
									</div>
									<div class="title-invoice font-bold" style="padding-bottom: 10px;padding-top:10px">HỢP ĐỒNG DU LỊCH</div>
									<div class="text-center width-full" style="padding-bottom: 10px;">
										<span>(TỔ CHỨC CHƯƠNG TRÌNH THAM QUAN DU LỊCH "</span>
										<span style="text-transform: uppercase;">
											<xsl:value-of select="TourName" />")
										</span>
									</div>
									<div class="font-italic">
										- Căn cứ Luật thương mại được Quốc hội nước Cộng hòa xã hội chủ nghĩa Việt Nam khóa XI, kỳ họp thứ VII thông qua ngày 14 tháng 06 năm 2005.
									</div>
									<div class="font-italic">
										- Căn cứ Bộ luật dân sự được Quốc hội nước cộng hòa xã hội chủ nghĩa Việt Nam khóa XIII thông qua ngày 24 tháng 11 năm 2015.
									</div>
									<div class="font-italic">
										- Căn cứ nhu cầu và khả năng của các bên.
									</div>
								</div>
							</div>
							<div class="content-block">
								<div>
									<div>
										<span>Hôm nay, </span>
										<xsl:variable name="issuedDate" select="CreatedTime" />
										<xsl:choose>
											<xsl:when test="$issuedDate != ''">
												<span>ngày</span>
												<span class="padding-left-4">
													<xsl:value-of select="substring($issuedDate, 9, 2)" />
												</span>
												<span class="padding-left-4">tháng</span>
												<span class="padding-left-4">
													<xsl:value-of select="substring($issuedDate, 6, 2)" />
												</span>
												<span class="padding-left-4">năm</span>
												<span class="padding-left-4">
													<xsl:value-of select="substring($issuedDate, 1, 4)" />
												</span>
											</xsl:when>
											<xsl:otherwise>
												<span class="date-text">ngày</span>
												<span>...</span>
												<span class="month-text padding-left-16 ">tháng</span>
												<span>...</span>
												<span class="year-text padding-left-16 ">năm</span>
												<span>...</span>
											</xsl:otherwise>
										</xsl:choose>
									</div>
									<div>Chúng tôi gồm có:</div>
									<div class="width-full flex-column" data-field="SideA">
										<div class="edit-item disable-hiden width-full type-2" style="">
											<div class="edit-label display-table-cell white-space-nowrap font-bold" style="min-width: 0px;">Bên A</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit font-bold" style="margin-left: 0px;">
												(KHÁCH DU LỊCH)
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideAName" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Người đại diện</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="CustomerName" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideAAddress" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Địa chỉ</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="CustomerAddress" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideAPhone" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Số điện thoại</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="CustomerPhone" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideAIdentitty" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">CMND/CCCD</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="CustomerIdentity" />
											</div>
										</div>
									</div>
									<div class="width-full flex-column" data-field="SideB">
										<div class="edit-item disable-hiden width-full type-2" style="">
											<div class="edit-label display-table-cell white-space-nowrap font-bold" style="min-width: 0px;">Bên B</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit font-bold" style="margin-left: 0px;">
												<xsl:value-of select="ProviderName" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideBAddress" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Địa chỉ</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="ProviderAddress" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideBName" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Người đại diện theo pháp luật công ty</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="Represent" />
											</div>
										</div>

										<div class="edit-item disable-hiden width-full type-2" data-field="SideBPost" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Chức vụ</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="RepresentPost" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideBPhone" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">Số điện thoại</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="RepresentPhone" />
											</div>
										</div>
										<div class="edit-item disable-hiden width-full type-2" data-field="SideBIdentitty" style="padding-left:10px">
											<div class="edit-label display-table-cell white-space-nowrap" style="min-width: 0px;">CMND/CCCD</div>
											<div class="two-dot display-table-cell white-space-nowrap" style="">:</div>
											<div class="edit-value display-table-cell none-edit" style="margin-left: 0px;">
												<xsl:value-of select="RepresentIdentity" />
											</div>
										</div>
									</div>
								</div>
								<div class="buyer-qr-infor invoice-third highlight-block width-full flex-column">
									<div class="font-bold">Hai bên thống nhất ký một số điều khoản phục vụ khách du lịch như sau:</div>
									<div class="font-bold">* Điều 1: Nội dung chương trình.</div>
									<div class="flex-column" style="padding-left: 10px">
										<xsl:variable name="startTime" select="ContractInfo/StartTime" />
										<xsl:variable name="endTime" select="ContractInfo/EndTime" />
										<div>
											<span class="font-bold">1. Thời gian từ</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($startTime, 12, 5)"/>,
											</span>
											<span>ngày</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($startTime, 9, 2)" />
											</span>
											<span class="padding-left-4">tháng</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($startTime, 6, 2)" />
											</span>
											<span class="padding-left-4">năm</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($startTime, 1, 4)" />;
											</span>
											<span>tới</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($endTime, 12, 5)"/>,
											</span>
											<span>ngày</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($endTime, 9, 2)" />
											</span>
											<span class="padding-left-4">tháng</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($endTime, 6, 2)" />
											</span>
											<span class="padding-left-4">năm</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring($endTime, 1, 4)" />.
											</span>
										</div>
										<div class="font-bold">2. Danh sách điểm tham quan</div>
										<div style="padding-left:10px;">
											<xsl:for-each select="ContractData/DestinationItem/Destination">
												<div class="flex-column">
													<div>
														* <xsl:value-of select="Name"/>:
													</div>
													<div style="padding-left:10px">
														<span>Địa điểm: </span>
														<span>
															<xsl:value-of select="Address"/>:
														</span>
													</div>
													<div style="padding-left:10px">
														<xsl:variable name="adultPrice" select="TicketPrice/Adult" />
														<xsl:variable name="childPrice" select="TicketPrice/Child" />
														<xsl:variable name="babyPrice" select="TicketPrice/Baby" />
														<span>Giá vé:</span>
														<span class="padding-left-4">người lớn</span>
														<span class="padding-left-4">
															<xsl:value-of select="format-number($adultPrice, '###,###.##')"/>đ,
														</span>
														<span class="padding-left-4">trẻ em</span>
														<span class="padding-left-4">
															<xsl:value-of select="format-number($childPrice, '###,###.##')"/>đ,
														</span>
														<xsl:choose>
															<xsl:when test="normalize-space($babyPrice) != ''">
																<span class="padding-left-4">em bé</span>
																<span class="padding-left-4">
																	<xsl:value-of select="format-number($babyPrice, '###,###.##')"/>đ.
																</span>
															</xsl:when>
														</xsl:choose>

													</div>
												</div>
											</xsl:for-each>
										</div>
										<div class="font-bold">3. Lịch trình</div>
										<div class="font-italic">Để đảm bảo tài sản và sự an toàn của Quý Khách, lái xe của công ty sẽ có trách nhiệm trả khách tại điểm mà xe đón khách lúc đầu.</div>
										<div class="font-bold">Điểm đón khách: <span><xsl:value-of select="PickupAdress"/></span></div>
										<div class="font-bold">
											<span>Thời gian đón khách:</span> 
											<span class="padding-left-4">
												<xsl:value-of select="substring(PickupTime, 12, 5)"/>,
											</span>
											<span>ngày</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring(PickupTime, 9, 2)" />
											</span>
											<span class="padding-left-4">tháng</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring(PickupTime, 6, 2)" />
											</span>
											<span class="padding-left-4">năm</span>
											<span class="padding-left-4">
												<xsl:value-of select="substring(PickupTime, 1, 4)" />.
											</span>
										</div>
										<xsl:choose>
											<xsl:when test="count(ContractData/Schedule/Day) > 0">
												<xsl:for-each select="ContractData/Schedule/Day">
													<div class="flex-column">
														<div class="font-bold">
															3.
															<span>
																<xsl:value-of select="SortOrder"/>.
															</span>
															<span class="padding-left-4">
																Ngày <xsl:value-of select="SortOrder"/>.
															</span>
														</div>
														<div class="font-bold">a. Buổi sáng.</div>
														<div class="flex-column" style="padding-left:10px">
															<xsl:for-each select="Morning/Activity">
																<xsl:variable name="startTimeActivity" select="StartTime" />
																<div>
																	* Thời gian:
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 12, 5)"/>,
																	</span>
																	<span>ngày</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 9, 2)" />
																	</span>
																	<span class="padding-left-4">tháng</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 6, 2)" />
																	</span>
																	<span class="padding-left-4">năm</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 1, 4)" />.
																	</span>
																</div>
																<div>
																	Địa điểm: <xsl:value-of select="Destination"/>
																</div>
																<div>
																	Hoạt động: <xsl:value-of select="Action"/>
																</div>
																<div style="padding: 10px 0"></div>
															</xsl:for-each>
														</div>
														<div class="font-bold">b. Buổi chiều.</div>
														<div class="flex-column" style="padding-left:10px">
															<xsl:for-each select="Afternoon/Activity">
																<xsl:variable name="startTimeActivity" select="StartTime" />
																<div>
																	* Thời gian:
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 12, 5)"/>,
																	</span>
																	<span>ngày</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 9, 2)" />
																	</span>
																	<span class="padding-left-4">tháng</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 6, 2)" />
																	</span>
																	<span class="padding-left-4">năm</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 1, 4)" />.
																	</span>
																</div>
																<div>
																	Địa điểm: <xsl:value-of select="Destination"/>
																</div>
																<div>
																	Hoạt động: <xsl:value-of select="Action"/>
																</div>
																<div style="padding: 10px 0"></div>
															</xsl:for-each>
														</div>
														<div class="font-bold">c. Buổi tối.</div>
														<div class="flex-column" style="padding-left:10px">
															<xsl:for-each select="Evening/Activity">
																<xsl:variable name="startTimeActivity" select="StartTime" />
																<div>
																	* Thời gian:
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 12, 5)"/>,
																	</span>
																	<span>ngày</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 9, 2)" />
																	</span>
																	<span class="padding-left-4">tháng</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 6, 2)" />
																	</span>
																	<span class="padding-left-4">năm</span>
																	<span class="padding-left-4">
																		<xsl:value-of select="substring($startTimeActivity, 1, 4)" />.
																	</span>
																</div>
																<div>
																	Địa điểm: <xsl:value-of select="Destination"/>
																</div>
																<div>
																	Hoạt động: <xsl:value-of select="Action"/>
																</div>
																<div style="padding: 10px 0"></div>
															</xsl:for-each>
														</div>
													</div>
												</xsl:for-each>
											</xsl:when>
										</xsl:choose>

									</div>
									<div class="font-bold" style="margin-top: 10px">* Điều 2: Số lượng khách.</div>
									<xsl:variable name="numberAdult">
										<xsl:choose>
											<xsl:when test="normalize-space(ContractInfo/NumberAdult) = ''">
												<xsl:value-of select="0"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="ContractInfo/NumberAdult"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:variable>
									<xsl:variable name="numberChild">
										<xsl:choose>
											<xsl:when test="normalize-space(ContractInfo/NumberChild) = ''">
												<xsl:value-of select="0"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="ContractInfo/NumberChild"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:variable>
									<xsl:variable name="numberBaby">
										<xsl:choose>
											<xsl:when test="normalize-space(ContractInfo/NumberBaby) = ''">
												<xsl:value-of select="0"/>
											</xsl:when>
											<xsl:otherwise>
												<xsl:value-of select="ContractInfo/NumberBaby"/>
											</xsl:otherwise>
										</xsl:choose>
									</xsl:variable>
									<xsl:variable name="totalTicketAdult" select="sum(ContractData/DestinationItem/Destination/TicketPrice/Adult)"/>
									<xsl:variable name="totalTicketChild" select="sum(ContractData/DestinationItem/Destination/TicketPrice/Child)"/>
									<xsl:variable name="totalTicketBaby" select="sum(ContractData/DestinationItem/Destination/TicketPrice/Baby)"/>
									<div>
										<span>- Số lượng khách: </span>
										<span>
											<xsl:value-of select="$numberAdult + $numberChild + $numberBaby"/>
										</span>
										<span>
											(Bao gồm:
										</span>
										<span>
											<xsl:value-of select="$numberAdult"/> người lớn,
										</span>
										<span>
											<xsl:value-of select="$numberChild"/> trẻ em,
										</span>
										<span>
											<xsl:value-of select="$numberBaby"/> em bé).
										</span>
									</div>
									<div class="font-italic">
										Nếu bên A giảm số lượng khách như trên hợp đồng đã ký là <span>
											<xsl:value-of select="$numberAdult + $numberChild + $numberBaby"/>
										</span> khách, bên A chịu 50% đơn giá mỗi khách giảm theo hợp đồng. Số lượng khách tăng được tính phát sinh theo đơn giá trên hợp đồng.
									</div>

									<div class="font-bold" style="margin-top: 10px">* Điều 3: Giá trị hợp đồng</div>
									<div>
										<span>
											- Giá cho 01 người lớn: <xsl:value-of select="format-number($totalTicketAdult, '###,###.##')"/> đ. Tổng số người lớn theo hợp đồng: <xsl:value-of select="$numberAdult"/> người.
										</span>
									</div>
									<div>
										<span>
											- Giá cho 01 trẻ em: <xsl:value-of select="format-number($totalTicketChild, '###,###.##')"/> đ. Tổng số trẻ em theo hợp đồng: <xsl:value-of select="$numberChild"/> người.
										</span>
									</div>
									<div>
										<span>
											- Giá cho 01 em bé: <xsl:value-of select="format-number($totalTicketBaby, '###,###.##')"/> đ. Tổng số em bé theo hợp đồng: <xsl:value-of select="$numberBaby"/> người.
										</span>
									</div>

									<xsl:for-each select="ContractData/AttachOption/Item">
										<div>
											<span>
												- <xsl:value-of select="Content"/>: 
											</span>
											<span>
												<xsl:value-of select="format-number(Cost, '###,###.##')"/> đ.
											</span>
										</div>
									</xsl:for-each>
									<div>Tổng cộng: <span class="font-bold"><xsl:value-of select="format-number(TotalCost, '###,###.##')"/></span> đ (Đã bao gồm 10% VAT)</div>
									<div>(Bằng chữ: 
										<span class="font-bold">
											<xsl:value-of select="TotalCostInWord"/>
										</span>).
									</div>
									<div class="font-italic">(Hợp đồng không gồm chi phí ăn ngủ của hành khách)</div>
									<div class="font-bold" style="margin-top: 10px">* Điều 4: Hình thức thanh toán</div>
									<div class="font-italic">Sau khi bên B thực hiện xong hợp đồng. Bên A có trách nhiệm thanh toán đầy đủ số tiền theo số lượng thực tế cho bên B tại văn phòng công ty.</div>

									<div class="font-bold" style="margin-top: 10px">* Điều 5: Điều kiện phạt hủy hợp đồng</div>
									<xsl:for-each select="ContractData/RefundPolicy/Item">
										<div class="d-flex" style="margin-top:5px;">
											<div>
												<xsl:value-of select="SortOrder"/>. 
											</div>
											<div style="padding-left: 5px;">
												<xsl:value-of select="Content"/>
											</div>
										</div>								
									</xsl:for-each>
								
									<div class="font-bold" style="margin-top: 10px">* Điều 6: Trách nhiệm của các bên</div>
									<xsl:for-each select="ContractData/Tutorial/Item">
										<div class="d-flex" style="margin-top:5px;">
											<div>
												<xsl:value-of select="SortOrder"/>. 
											</div>
											<div style="padding-left: 5px;">
												<xsl:value-of select="Content"/>
											</div>
										</div>								
									</xsl:for-each>
								</div>
							</div>

							<div class="sign-xml-block width-full" style="margin-top: 20px">
								<div class="d-flex width-full">
									<div class="flex-column width-half" data-field="BuyerSign">
										<div class="font-bold width-full" style="">ĐẠI DIỆN BÊN A</div>
										<div class="sign-content buyer-sign-content width-full" style="">
										
										</div>
									</div>
									<div class="flex-column width-half" data-field="SellerSign" style="margin-left: 50px">
										<div class="font-bold width-full" style="">ĐẠI DIỆN BÊN B</div>
										<div class="sign-content seller-sign-content width-full" style="">
										
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="fakeContent"></div>
				</div>
			</body>
		</html>
	</xsl:template>
	
	<xsl:template name="reverse">
		<xsl:param name="input" />
		<xsl:variable name="length" select="string-length($input)" />
		<xsl:choose>
			<xsl:when test="$length &lt; 2">
				<xsl:value-of select="$input" />
			</xsl:when>
			<xsl:when test="$length = 2">
				<xsl:value-of select="substring($input,2,1)" />
				<xsl:value-of select="substring($input,1,1)" />
			</xsl:when>
			<xsl:otherwise>
				<xsl:value-of select="substring($input, $length,1)" />
				<xsl:call-template name="reverse">
					<xsl:with-param name="input" select="substring($input, 2, $length - 2)" />
				</xsl:call-template>
				<xsl:value-of select="substring($input,1,1)" />
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	
	<xsl:strip-space elements="*" />
</xsl:stylesheet>