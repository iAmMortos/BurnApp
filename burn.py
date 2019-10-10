from fire_view import FireView

if __name__ == '__main__':
	FireView.load_view().present(orientations=['portrait','portrait_upside_down'], animated=False, hide_title_bar=True, style='full_screen')
