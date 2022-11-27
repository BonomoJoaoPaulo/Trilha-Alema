import sys

from Abstractions.AbstractConnection import AbstractConnection
from Abstractions.AbstractMove import AbstractMove
from Abstractions.AbstractPiece import AbstractPiece
from Abstractions.AbstractPlayer import AbstractPlayer
from Abstractions.AbstractPosition import AbstractPosition
from Abstractions.AbstractBoard import AbstractBoard
from Abstractions.AbstractPlayerInterface import AbstractPlayerInterface
from Abstractions.AbstractInterfaceUpdater import AbstractInterfaceUpdater

from Game.Connection import Connection
# from Game.Move import Move
from Game.Piece import Piece
# from Game.Player import Player
from Game.Position import Position

#from Interface.InterfaceUpdater import InterfaceUpdater
#from Interface.PlayerInterface import PlayerInterface

class Board:
	def __init__(self, local_player: AbstractPlayer, remote_player: AbstractPlayer, player_interface: AbstractPlayerInterface) -> None:
		self.__player_interface: AbstractPlayerInterface = player_interface
		self.__position_matrix: list = self.set_board_position_matrix()
		self.__occupied_positions: list[AbstractPosition] = []
		self.__total_positions: int = 32
		self.__selected_position: AbstractPosition = None
		self.__selected_piece: AbstractPiece = None
		self.__local_player = local_player # Player(1, "name", True, "styles") CHANGE "name" AND "styles"
		self.__remote_player = remote_player # Player(2, "name", False, "styles") CHANGE "name " AND "styles"
		self.__draw: bool = False
		self.__withdrawed: bool = False
		self.__game_phase: str = "placing"
		self.__move_type: str = None
		self.__move: AbstractMove = None

	@property
	def player_interface(self) -> AbstractPlayerInterface:
		return self.__player_interface
	
	@property
	def interface_updater(self) -> None:
		return self.__interface_updater
	
	@property
	def position_matrix(self) -> list:
		return self.__position_matrix
	
	@property
	def occupied_positions(self) -> list[AbstractPosition]:
		return self.__occupied_positions

	@occupied_positions.setter
	def occupied_positions(self, occupied__positions_list: list[AbstractPosition]):
		self.__occupied_positions = occupied__positions_list
	
	@property
	def total_positions(self) -> int:
		return self.__total_positions
	
	@property
	def selected_position(self) -> AbstractPosition:
		return self.__selected_position
	
	@selected_position.setter
	def selected_position(self, selected_position: AbstractPosition):
		self.__selected_position = selected_position
	
	@property
	def selected_piece(self) -> AbstractPiece:
		return self.__selected_piece
	
	@selected_piece.setter
	def selected_piece(self, selected_piece: AbstractPiece):
		self.__selected_piece = selected_piece
	
	@property
	def local_player(self) -> AbstractPlayer:
		return self.__local_player
	
	@local_player.setter
	def local_player(self, local_player: AbstractPlayer):
		self.__local_player = local_player
	
	@property
	def remote_player(self) -> AbstractPlayer:
		return self.__remote_player
	
	@remote_player.setter
	def remote_player(self, remote_player: AbstractPlayer):
		self.__remote_player = remote_player

	@property
	def draw(self) -> bool:
		return self.__draw
	
	@draw.setter
	def draw(self, draw: bool):
		self.__draw = draw

	@property
	def withdrawed(self) -> bool:
		return self.__withdrawed
	
	@withdrawed.setter
	def withdrawed(self, withdrawed: bool) -> None:
		self.__withdrawed = withdrawed

	@property
	def game_phase(self) -> str:
		return self.__game_phase

	@game_phase.setter
	def game_phase(self, phase : str):
		self.__game_phase = phase

	@property
	def move_type(self) -> str:
		return self.__move_type

	@move_type.setter
	def move_type(self, move_type: str):
		self.__move_type = move_type

	@property
	def move(self) -> AbstractMove:
		return self.__move

	@move.setter
	def move(self, move: AbstractMove):
		self.move = move

	def set_board_position_matrix(self) -> list:
		position_1 = Position((0, 1))
		position_2 = Position((0, 2))
		position_3 = Position((0, 3))
		position_4 = Position((1, 2))
		position_5 = Position((1, 3))
		position_6 = Position((1, 4))
		position_7 = Position((1, 6))
		position_8 = Position((2, 1))
		position_9 = Position((2, 2))
		position_10 = Position((2, 3))
		position_11 = Position((2, 4))
		position_12 = Position((2, 5))
		position_13 = Position((2, 6))
		position_14 = Position((3, 0))
		position_15 = Position((3, 1))
		position_16 = Position((3, 2))
		position_17 = Position((3, 4))
		position_18 = Position((3, 5))
		position_19 = Position((3, 6))
		position_20 = Position((4, 0))
		position_21 = Position((4, 1))
		position_22 = Position((4, 2))
		position_23 = Position((4, 3))
		position_24 = Position((4, 4))
		position_25 = Position((4, 5))
		position_26 = Position((5, 0))
		position_27 = Position((5, 2))
		position_28 = Position((5, 3))
		position_29 = Position((5, 4))
		position_30 = Position((6, 3))
		position_31 = Position((6, 4))
		position_32 = Position((6, 5))

		#Sets the neighbors of each position
		position_1.neighborhood = [position_2, position_4]
		position_2.neighborhood = [position_1, position_3, position_5]
		position_3.neighborhood = [position_2, position_6]
		position_4.neighborhood = [position_1, position_5, position_8, position_10]
		position_5.neighborhood = [position_2, position_4, position_6, position_11]
		position_6.neighborhood = [position_3, position_5, position_12]
		position_7.neighborhood = [position_12, position_13]
		position_8.neighborhood = [position_4, position_14, position_15]
		position_9.neighborhood = [position_10, position_15, position_16]
		position_10.neighborhood = [position_4, position_9, position_11]
		position_11.neighborhood = [position_5, position_10, position_17]
		position_12.neighborhood = [position_6, position_7, position_17, position_18]
		position_13.neighborhood = [position_7, position_18, position_19]
		position_14.neighborhood = [position_8, position_20]
		position_15.neighborhood = [position_8, position_9, position_20, position_21]
		position_16.neighborhood = [position_9, position_21, position_22]
		position_17.neighborhood = [position_11, position_12, position_24]
		position_18.neighborhood = [position_12, position_13, position_24, position_25]
		position_19.neighborhood = [position_13, position_25]
		position_20.neighborhood = [position_14, position_15, position_26]
		position_21.neighborhood = [position_15, position_16, position_26, position_27]
		position_22.neighborhood = [position_16, position_2, position_28]
		position_23.neighborhood = [position_22, position_24, position_29]
		position_24.neighborhood = [position_17, position_18, position_23]
		position_25.neighborhood = [position_18, position_19, position_29]
		position_26.neighborhood = [position_20, position_21]
		position_27.neighborhood = [position_21, position_28, position_30]
		position_28.neighborhood = [position_22, position_27, position_29, position_31]
		position_29.neighborhood = [position_23, position_25, position_28, position_32]
		position_30.neighborhood = [position_27, position_31]
		position_31.neighborhood = [position_28, position_30, position_32]
		position_32.neighborhood = [position_29, position_31]
  
		#Instantiating all the connections (moinhos)
		connection_1 = Connection(1, [position_1, position_2, position_3])
		connection_2 = Connection(2, [position_4, position_5, position_6])
		connection_3 = Connection(3, [position_9, position_10, position_11])
		connection_4 = Connection(4, [position_22, position_23, position_24])
		connection_5 = Connection(5, [position_27, position_28, position_29])
		connection_6 = Connection(6, [position_30, position_31, position_32])
		connection_7 = Connection(7, [position_1, position_4, position_10])
		connection_8 = Connection(8, [position_2, position_5, position_11])
		connection_9 = Connection(9, [position_3, position_6, position_12])
		connection_10 = Connection(10, [position_21, position_27, position_30])
		connection_11 = Connection(11, [position_22, position_28, position_31])
		connection_12 = Connection(12, [position_23, position_29, position_32])
		connection_13 = Connection(13, [position_4, position_8, position_14])
		connection_14 = Connection(14, [position_9, position_15, position_20])
		connection_15 = Connection(15, [position_16, position_21, position_26])
		connection_16 = Connection(16, [position_7, position_12, position_17])
		connection_17 = Connection(17, [position_13, position_18, position_24])
		connection_18 = Connection(18, [position_19, position_25, position_29])
		connection_19 = Connection(19, [position_14, position_20, position_26])
		connection_20 = Connection(20, [position_8, position_15, position_21])
		connection_21 = Connection(21, [position_9, position_16, position_22])
		connection_22 = Connection(22, [position_11, position_17, position_24])
		connection_23 = Connection(23, [position_12, position_18, position_25])
		connection_24 = Connection(24, [position_7, position_13, position_19])

		#Sets the connections of each position
		position_1.connections = [connection_1, connection_7]
		position_2.connections = [connection_1, connection_8]
		position_3.connections = [connection_1, connection_9]
		position_4.connections = [connection_2, connection_7, connection_13]
		position_5.connections = [connection_2, connection_8]
		position_6.connections = [connection_2, connection_9]
		position_7.connections = [connection_16, connection_24]
		position_8.connections = [connection_13, connection_20]
		position_9.connections = [connection_3, connection_14, connection_21]
		position_10.connections = [connection_3, connection_7]
		position_11.connections = [connection_3, connection_8, connection_22]
		position_12.connections = [connection_9, connection_16, connection_23]
		position_13.connections = [connection_17, connection_24]
		position_14.connections = [connection_13, connection_19]
		position_15.connections = [connection_14, connection_20]
		position_16.connections = [connection_15, connection_21]
		position_17.connections = [connection_16, connection_22]
		position_18.connections = [connection_17, connection_23]
		position_19.connections = [connection_18, connection_24]
		position_20.connections = [connection_14, connection_19]
		position_21.connections = [connection_10, connection_15, connection_20]
		position_22.connections = [connection_4, connection_11, connection_21]
		position_23.connections = [connection_4, connection_12]
		position_24.connections = [connection_4, connection_17, connection_22]
		position_25.connections = [connection_18, connection_23]
		position_26.connections = [connection_15, connection_19]
		position_27.connections = [connection_5, connection_10]
		position_28.connections = [connection_5, connection_11]
		position_29.connections = [connection_5, connection_12, connection_18]
		position_30.connections = [connection_6, connection_10]
		position_31.connections = [connection_6, connection_11]
		position_32.connections = [connection_6, connection_12]
  
		position_matrix = [
			[None, position_1, position_2, position_3, None, None, None],
   			[None, None, position_4, position_5, position_6, None, position_7],
			[None, position_8, position_9, position_10, position_11, position_12, position_13],
			[position_14, position_15, position_16, None, position_17, position_18, position_19],
			[position_20, position_21, position_22, position_23, position_24, position_25, None],
			[position_26, None, position_27, position_28, position_29, None, None],
			[None, None, None, position_30, position_31, position_32, None]
		]

		return position_matrix

	# Só entra aqui em colocacao de peca LOCAL
	def place_piece(self) -> None: # Atualizar modelagem
		is_turn = self.__local_player.turn
		if not is_turn:
			self.__player_interface.notify_player("Sorry, but is not your turn.")
		else:
			self.__move.set_move_none()
			self.__move.set_move("place_piece", self.__local_player.player_id, final_position = self.__selected_position)
			piece_to_place = Piece(self.__local_player)
			self.execute_place_piece(piece_to_place)
			if self.__local_player.pieces_in_hand == 0:
				self.set_game_phase("moving")

			self.evaluate_moinho()

	# Só entra aqui em movimentacao de peca LOCAL
	def move_piece(self) -> None:
		is_turn = self.__local_player.turn
		if not is_turn:
			self.__player_interface.notify_player("Sorry, but is not your turn.")
		else:
			piece_to_move = self.__selected_piece
			piece_owner = piece_to_move.owner_player

			if piece_owner != self.__local_player:
				self.__player_interface.notify_player("You can't move a opponent piece.")
			else:
				self.__move.set_move_none()
				if not self.__selected_position.is_occupied:
					if (self.__selected_position in piece_to_move.position.neighborhood) or piece_owner.can_do_fly(): # Alterar modelagem
						self.__move.set_move("move_piece", self.__local_player.player_id, final_position = self.__selected_position, 
											start_position = self.__selected_piece.position)
						self.execute_move_piece()
						self.evaluate_moinho()
				else:
					self.__player_interface.notify_player("You're clicking on a occupied position.")

	# Só entra aqui em retirada de peca feita pelo player LOCAL
	def remove_piece(self, num_of_moinhos: int) -> None: # ALTERAR MODELAGEM
		piece_to_remove: AbstractPiece = self.__selected_piece
		piece_owner: AbstractPlayer = piece_to_remove.owner_player

		if piece_owner == self.__remote_player:
			in_moinho = piece_to_remove.in_moinho

			if in_moinho:
				can_remove: bool = (self.__remote_player.pieces_on_board == 3)
			else:
				can_remove: bool = True

			if can_remove:
				self.execute_remove_piece(self.__selected_piece.position, self.__selected_piece.owner_player)	
				move_type = self.__move.type
				if move_type == "place_piece":
					self.__move.set_move("place_piece_and_remove_piece", self.__local_player.player_id, num_of_moinhos,
										removed_piece_position = piece_to_remove.position)
				elif move_type == "move_piece":
					self.__move.set_move("move_piece_and_remove_piece", self.__local_player.player_id, num_of_moinhos,
										removed_piece_position = piece_to_remove.position)
				
				if num_of_moinhos == 1:
					self.__player_interface.send_move(self.__move)
					self.evaluate_winner()
					self.finish_turn()

			else:
				self.__player_interface.notify_player("You can't remove a piece that's part of a moinho.")

		else:
			self.__player_interface.notify_player("You can't remove your own piece.")

	# Só entra aqui em colocação
	def execute_place_piece(self, piece_put: AbstractPiece) -> None: # Alterar modelagem
		owner_player_of_piece: AbstractPlayer = piece_put.owner_player
		owner_player_of_piece.decrement_pieces_in_hand() # Alterar modelagem
		owner_player_of_piece.increment_pieces_on_board() # Alterar modelagem

		self.__selected_position.place_piece(piece_put)

		self.__player_interface.update_interface_image()
	
	# Só entra aqui em movimentação
	def execute_move_piece(self) -> None: # Alterar modelagem
		piece_to_move = self.__selected_piece
		destiny_position = self.__selected_position
		origin_position = piece_to_move.position

		origin_position.remove_piece()
		destiny_position.place_piece(piece_to_move)

		self.__player_interface.update_interface_image()

	# Só entra aqui em remoção de peca
	def execute_remove_piece(self, position_to_remove_piece: AbstractPosition, player_who_removed_piece: AbstractPlayer) -> None: # Alterar modelagem
		piece_to_remove = position_to_remove_piece.piece
		player_to_decrement_pieces_in_board = position_to_remove_piece.player_on_pos
		
		piece_to_remove.set_piece_captured()
		player_to_decrement_pieces_in_board.decrement_pieces_on_board()
		player_who_removed_piece.increment_removed_pieces()
		position_to_remove_piece.remove_piece()

		self.__player_interface.update_interface_image()

	def evaluate_moinho(self) -> None:
		num_of_moinhos: int = self.get_num_of_moinhos(self.__selected_position)
		self.__move.moinhos = num_of_moinhos
		piece_put_on_position: AbstractPiece = self.__selected_position.piece
  
		if num_of_moinhos == 0:
			self.evaluate_winner()
			self.finish_turn()
			piece_put_on_position.in_moinho: bool = False
			self.__move.moinho: int = num_of_moinhos
			self.__player_interface.send_move(self.__move)
		
		elif num_of_moinhos > 0:
			self.__player_interface.notify_player(f"You have done {num_of_moinhos} moinho(s). Remove a opponent piece.")

	def get_num_of_moinhos(self, selected_position: AbstractPosition) -> int: # Change argument's name in modelling
		position_connections: list[AbstractConnection] = selected_position.connections
		player_on_selected_position: AbstractPlayer = selected_position.player_on_pos
  
		moinhos_count = 0
		for connection in position_connections:
			positions_in_connection = connection.positions

			same_player = 0
			for position in positions_in_connection:
				if position.player_on_pos == player_on_selected_position:
					same_player += 1

			if same_player == 3:
				moinhos_count += 1
		
		return moinhos_count

	def start_match(self, local_player: AbstractPlayer, remote_player: AbstractPlayer, local_player_id: int) -> None:
		pass

	def execute_move(self, move_to_execute: AbstractMove) -> None:
		self.__move = move_to_execute
		move_type = self.__move.type

		if move_type == "place_piece":
			self.execute_place_piece()

		elif move_type == "move_piece":
			self.execute_move_piece()

		elif move_type == "place_piece_and_remove_piece":
			self.execute_place_piece()
			self.execute_remove_piece()

		elif move_type == "move_piece_and_remove_piece":
			self.execute_move_piece()
			self.execute_remove_piece()

		elif move_type == "propose_draw":
			accepts_draw: bool = self.__player_interface.ask_user_accepts_draw() # MUDAR NOME NA MODELAGEM

			if accepts_draw:
				self.__move.set_move("accept_draw", self.__local_player.player_id)
				self.__player_interface.send_move(self.__move)
			else:
				self.__move.set_move("decline_draw", self.__local_player.player_id)
				self.__player_interface.send_move(self.__move)
		
		elif move_type == "accept_draw":
			self.set_draw()
		
		elif move_type == "decline_draw":
			self.restart_move()

		self.evaluate_winner()
		self.__player_interface.notify_player("IT'S YOUR TURN.")
		self.finish_turn()
	
	def set_draw(self) -> None:
		self.__draw = True
		self.end_game()

	def end_game(self) -> None:
		if self.__local_player.winner:
			self.__player_interface.notify_player("CONGRATULATIONS! YOU WON THE GAME!")
		elif self.__remote_player.winner:
			self.__player_interface.notify_player("SAD, YOU LOST THE GAME! TRY HARDER NEXT TIME.")
		else:
			self.__player_interface.notify_player("OH, SO BORING... THE GAME ENDED IN DRAW.")
		
		sys.exit()

	def restart_move(self) -> None:
		self.__move.set_move_none()

	def receive_withdrawal_notification(self) -> None:
		self.set_abandoned()
		self.set_winner(self.__local_player)
		self.end_game()

	def finish_turn(self) -> None:
		self.__local_player.change_turn()
		self.__remote_player.change_turn()

	def reset_match(self) -> None:
		pass

	def clicked_position(self, line:int, column:int) -> None:
		#To properly implement a piece movement, two clicks are needed.
		#Hence, if game_phase == "moving":
		#Check if piece to move has already been set, if piece_to_move_already_set:
		#Save second click as selected_position (which is the destiny). Then, do the movement as already modelled.
		print(f"Clicked position: {line}, {column}")
		game_phase: str = self.__game_phase
		position : AbstractPosition = self.__position_matrix[line][column]
		occupied: bool = position.is_occupied
		moinhos: int = self.__move.moinhos
		if game_phase == "placing" and not occupied and not moinhos:
			self.__selected_position = position
			self.place_piece()

		if game_phase == "moving" and occupied and not moinhos:
			if self.__selected_piece == None:
				self.__selected_piece = position.piece
			else:
				self.__selected_position = position
				self.move_piece()

		if moinhos:
			self.__selected_piece = position.piece
			self.remove_piece()
			moinhos -= 1
			self.__player_interface.notify_player(f"You can remove more {moinhos} pieces.")

	def get_interface_changes(self) -> tuple:
		pass

	def check_if_match_was_abandoned(self) -> bool:
		pass

	def set_abandoned(self) -> None:
		self.__withdrawed = True

	def clicked_propose_draw(self) -> None:
		print("Clicked on propose draw button.")
		is_turn: bool = self.__local_player.turn
		if is_turn:
			# self.propose_draw() RETIRAR DO CODIGO E DA MODELAGEM
			self.__move.set_move("propose_draw", self.__local_player.player_id)
			self.__player_interface.send_move(self.__move)
			self.finish_turn()
			self.__player_interface.update_interface_image()
		else:
			pass

	def set_winner(self, winner_player: AbstractPlayer) -> None:
		winner_player.winner = True

	def verify_blocked(self, player: AbstractPlayer) -> bool:
		blocked_pieces_count: int = 0
		player_pieces_number: int = player.pieces_on_board

		for position in self.__position_matrix:
			if (position is not None) and (position.player_on_pos == player):
				position_neighborhood: list[AbstractPosition] = position.neighborhood
				occupied_neighbors = 0
				for neighbor in position_neighborhood:
					if neighbor.is_occupied:
						occupied_neighbors += 1
				if occupied_neighbors == len(position_neighborhood):
					blocked_pieces_count += 1
		
		is_player_blocked = (player_pieces_number == blocked_pieces_count)
		return is_player_blocked

	def evaluate_winner(self) -> None:
		local_player = self.__local_player
		remote_player = self.__remote_player

		remote_player_has_sufficient_pieces: bool = remote_player.verify_sufficient_pieces_number()
		remote_player_blocked: bool = self.verify_blocked(remote_player)

		local_player_has_sufficient_pieces: bool = local_player.verify_sufficient_pieces_number()
		local_player_blocked: bool = self.verify_blocked(local_player)

		if remote_player_blocked or not remote_player_has_sufficient_pieces: # Alterar diagrama de algoritmo
			self.set_winner(local_player)
			self.end_game()
		elif local_player_blocked or not local_player_has_sufficient_pieces:
			self.set_winner(remote_player)
			self.end_game()
		else:
			pass
